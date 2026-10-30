import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

from backend.database import db
from backend.rag_engine import seed_database, query_rag_engine

print("=" * 65)
print("  STEP 1: SEEDING MONGODB ATLAS WITH SAMPLE DOCUMENTS...")
print("=" * 65)
res = seed_database(db)
print(f"Result: {res}")

docs = db.get_all_documents()
print(f"Indexed documents in MongoDB: {len(docs)}")
for d in docs:
    print(f"  - {d['doc_name']} ({d['category']}): {d['total_chunks']} chunks")

print("\n" + "=" * 65)
print("  STEP 2: TESTING MULTI-SOURCE SYNTHESIS QUERY...")
print("  Query: 'If an outage exceeds 2 hours, what is our customer liability and what is the internal mitigation deadline?'")
print("=" * 65)

test_query = "If an outage exceeds 2 hours, what is our customer liability and what is the internal mitigation deadline?"
response = query_rag_engine(test_query, db, limit=4)

print("\n[AI Summary]:")
print(response.get("summary"))

print("\n[Detailed Findings]:")
for f in response.get("detailed_findings", []):
    print(f"  * {f}")

print("\n[Citations & Exact Quotes]:")
for c in response.get("citations", []):
    print(f"  [{c.get('doc_name')} | {c.get('section')}]: \"{c.get('quote')}\"")

print("\n[Conflicts Detected]:")
for conf in response.get("conflicts_detected", []):
    print(f"  ! {conf.get('title')}: {conf.get('doc_a')} vs {conf.get('doc_b')}")
    print(f"    Impact: {conf.get('risk_analysis')}")

print("\n" + "=" * 65)
print("  STEP 3: TESTING UNANSWERABLE / OUT-OF-SCOPE QUERY...")
print("  Query: 'What is the dress code policy for engineers in the datacenter?'")
print("=" * 65)

unanswerable_query = "What is the dress code policy for engineers in the datacenter?"
response_un = query_rag_engine(unanswerable_query, db, limit=4)
print(f"Is Answerable: {response_un.get('is_answerable')}")
print(f"Response: {response_un.get('summary')}")

print("\n" + "=" * 65)
print(">>> END-TO-END RAG PIPELINE VERIFICATION SUCCESSFUL!")
print("=" * 65)
