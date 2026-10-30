import os
from typing import List, Dict, Any, Optional
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "auditlens_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "documents")
INDEX_NAME = os.getenv("INDEX_NAME", "vector_index")

class Database:
    def __init__(self):
        if not MONGODB_URI:
            raise ValueError("MONGODB_URI is not set in environment variables.")
        self.client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

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

    def vector_search(self, query_vector: List[float], limit: int = 5, filter_doc: Optional[str] = None) -> List[Dict[str, Any]]:
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

        # Optional metadata filter if specified
        if filter_doc:
            search_stage["filter"] = {"doc_id": filter_doc}

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
                    "score": {"$meta": "vectorSearchScore"}
                }
            }
        ]

        cursor = self.collection.aggregate(pipeline)
        return list(cursor)

    def get_all_documents(self) -> List[Dict[str, Any]]:
        """List distinct documents and their chunk counts."""
        pipeline = [
            {
                "$group": {
                    "_id": "$doc_id",
                    "doc_name": {"$first": "$doc_name"},
                    "category": {"$first": "$category"},
                    "total_chunks": {"$sum": 1}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "doc_id": "$_id",
                    "doc_name": 1,
                    "category": 1,
                    "total_chunks": 1
                }
            }
        ]
        return list(self.collection.aggregate(pipeline))

    def clear_all(self):
        """Reset the collection for fresh demonstrations."""
        return self.collection.delete_many({})

db = Database()
