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

    def get_user_history(self, user_email: Optional[str] = None, limit: int = 15) -> List[Dict[str, Any]]:
        """Retrieve recent audit queries."""
        query = {}
        if user_email and user_email != "guest":
            query["user_email"] = user_email
        cursor = self.history_col.find(query, {"_id": 0}).sort("created_at", -1).limit(limit)
        return list(cursor)

    def get_all_raw_chunks(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get sample chunks for cross-document conflict scanning."""
        cursor = self.collection.find({}, {"_id": 0, "embedding": 0}).limit(limit)
        return list(cursor)

db = Database()
