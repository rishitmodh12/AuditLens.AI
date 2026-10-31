import os
from typing import List, Dict, Any, Optional
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "").strip('"').strip("'")
DATABASE_NAME = os.getenv("DATABASE_NAME", "auditlens_db").strip('"').strip("'")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "documents").strip('"').strip("'")
INDEX_NAME = os.getenv("INDEX_NAME", "vector_index").strip('"').strip("'")

class Database:
    def __init__(self):
        if not MONGODB_URI:
            raise ValueError("MONGODB_URI is not set in environment variables.")
        self.client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]
        self.users_col = self.db["users"]
        self.history_col = self.db["audit_history"]

    def ping(self) -> bool:
        try:
            self.client.admin.command("ping")
            return True
        except Exception:
            return False

    def insert_chunks(self, chunks: List[Dict[str, Any]]) -> int:
        """Insert embedded document chunks into MongoDB."""
        if not chunks:
            return 0
        result = self.collection.insert_many(chunks)
        return len(result.inserted_ids)

    def vector_search(self, query_vector: List[float], limit: int = 5, user_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Execute MongoDB Atlas $vectorSearch aggregation pipeline.
        Searches semantic embeddings with score calculation.
        """
        search_stage: Dict[str, Any] = {
            "index": INDEX_NAME,
            "path": "embedding",
            "queryVector": query_vector,
            "numCandidates": 50,
            "limit": limit
        }

        pipeline = [
            {"$vectorSearch": search_stage},
            {
                "$project": {
                    "_id": 0,
                    "chunk_id": 1,
                    "doc_id": 1,
                    "doc_name": 1,
                    "category": 1,
                    "section": 1,
                    "text": 1,
                    "user_id": 1,
                    "score": {"$meta": "vectorSearchScore"}
                }
            }
        ]

        cursor = self.collection.aggregate(pipeline)
        return list(cursor)

    def hybrid_search(self, query_text: str, query_vector: List[float], limit: int = 5, user_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Execute Hybrid Search combining MongoDB Atlas $vectorSearch (semantic) 
        with keyword lexical scoring (exact clause numbers, currency, and regulatory entities).
        """
        import re
        # 1. Fetch semantic candidates via Atlas $vectorSearch
        vector_candidates = self.vector_search(query_vector, limit=max(limit * 2, 8), user_id=user_id)
        if not vector_candidates:
            return []

        # 2. Extract lexical key terms from query
        tokens = set(re.findall(r'[A-Za-z0-9_.\-₹]+', query_text.lower()))
        critical_terms = {"cert-in", "sev-1", "severity-1", "dpdp", "rbi", "4.2", "3.2", "1.1", "4.1", "8.5", "6.3", "7.4", "₹75,000", "₹1,50,000", "₹50,000", "mumbai"}

        # 3. Score each chunk with hybrid fusion
        scored_results = []
        for chunk in vector_candidates:
            v_score = float(chunk.get("score", 0.0))
            chunk_content = (chunk.get("text", "") + " " + chunk.get("section", "")).lower()

            # Count keyword hits
            matches = [t for t in tokens if len(t) > 2 and t in chunk_content]
            crit_matches = [t for t in critical_terms if t in query_text.lower() and t in chunk_content]

            lexical_score = min(1.0, (len(matches) * 0.15) + (len(crit_matches) * 0.40))

            # Reciprocal / weighted fusion
            hybrid_score = round((0.70 * v_score) + (0.30 * lexical_score), 4)

            chunk["vector_score"] = round(v_score, 4)
            chunk["lexical_score"] = round(lexical_score, 4)
            chunk["hybrid_score"] = hybrid_score
            chunk["matched_terms"] = crit_matches or matches[:4]
            scored_results.append(chunk)

        # 4. Re-rank by hybrid score
        scored_results.sort(key=lambda x: x["hybrid_score"], reverse=True)
        return scored_results[:limit]

    def get_all_documents(self, user_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """List distinct documents and their chunk counts."""
        match_stage = {}
        if user_id:
            # Return global sample docs + user's uploaded docs
            match_stage = {"$or": [{"user_id": None}, {"user_id": user_id}, {"user_id": "system"}]}

        pipeline = []
        if match_stage:
            pipeline.append({"$match": match_stage})

        pipeline.extend([
            {
                "$group": {
                    "_id": "$doc_id",
                    "doc_name": {"$first": "$doc_name"},
                    "category": {"$first": "$category"},
                    "total_chunks": {"$sum": 1},
                    "uploaded_at": {"$first": "$uploaded_at"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "doc_id": "$_id",
                    "doc_name": 1,
                    "category": 1,
                    "total_chunks": 1,
                    "uploaded_at": 1
                }
            }
        ])
        return list(self.collection.aggregate(pipeline))

    def delete_document(self, doc_id: str) -> int:
        """Delete all chunks belonging to a specific document."""
        result = self.collection.delete_many({"doc_id": doc_id})
        return result.deleted_count

    def clear_all(self):
        """Reset the document collection."""
        return self.collection.delete_many({})

    # USER PROFILE OPERATIONS
    def upsert_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save or update user profile upon login."""
        email = user_data.get("email")
        if not email:
            raise ValueError("Email required")
        user_data["updated_at"] = datetime.utcnow().isoformat()
        self.users_col.update_one(
            {"email": email},
            {"$set": user_data, "$setOnInsert": {"created_at": datetime.utcnow().isoformat()}},
            upsert=True
        )
        saved = self.users_col.find_one({"email": email}, {"_id": 0})
        return saved or user_data

    def get_user(self, email: str) -> Optional[Dict[str, Any]]:
        return self.users_col.find_one({"email": email}, {"_id": 0})

    def update_user_preferences(self, email: str, updates: Dict[str, Any]):
        self.users_col.update_one({"email": email}, {"$set": updates})

    # AUDIT HISTORY OPERATIONS
    def save_audit_history(self, record: Dict[str, Any]) -> str:
        """Save an audit run for user history."""
        record["created_at"] = datetime.utcnow().isoformat()
        res = self.history_col.insert_one(record)
        return str(res.inserted_id)

    def get_user_history(self, user_email: Optional[str] = None, limit: int = 25) -> List[Dict[str, Any]]:
        """Retrieve recent audit queries with stringified ID."""
        query = {}
        if user_email and user_email != "guest":
            query["user_email"] = user_email
        cursor = self.history_col.find(query).sort("created_at", -1).limit(limit)
        results = []
        for doc in cursor:
            doc["id"] = str(doc["_id"])
            del doc["_id"]
            results.append(doc)
        return results

    def delete_single_history(self, record_id: str, user_email: Optional[str] = None) -> bool:
        """Permanently delete an individual audit history item."""
        from bson import ObjectId
        try:
            query: Dict[str, Any] = {"_id": ObjectId(record_id)}
            if user_email and user_email != "guest":
                query["user_email"] = user_email
            res = self.history_col.delete_one(query)
            return res.deleted_count > 0
        except Exception:
            return False

    def clear_all_history(self, user_email: Optional[str] = None) -> int:
        """Permanently clear audit history for the current user."""
        query = {}
        if user_email and user_email != "guest":
            query["user_email"] = user_email
        res = self.history_col.delete_many(query)
        return res.deleted_count

    def get_all_raw_chunks(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get sample chunks for cross-document conflict scanning."""
        cursor = self.collection.find({}, {"_id": 0, "embedding": 0}).limit(limit)
        return list(cursor)

db = Database()
