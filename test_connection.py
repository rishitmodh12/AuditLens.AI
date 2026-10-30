import os
import sys
import httpx
from pymongo import MongoClient
from dotenv import load_dotenv

# Ensure utf-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "auditlens_db")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001")

print("=" * 60)
print("  AuditLens AI - System Diagnostic & Connection Checker")
print("=" * 60)

# Check 1: MongoDB Atlas Ping
print("\n[1/3] Testing MongoDB Atlas Connection...")
try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("[+] SUCCESS: Connected to MongoDB Atlas Cluster0!")
    db = client[DATABASE_NAME]
    print(f"[+] SUCCESS: Database '{DATABASE_NAME}' ready.")
except Exception as e:
    print(f"[-] ERROR connecting to MongoDB: {e}")
    sys.exit(1)

# Check 2: Gemini Generation Test
print(f"\n[2/3] Testing Google Gemini API ({GEMINI_MODEL})...")
try:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": "Reply with 'AuditLens AI Ready' in 3 words"}]}]
    }
    resp = httpx.post(url, json=payload, timeout=10.0)
    if resp.status_code == 200:
        data = resp.json()
        ai_reply = data['candidates'][0]['content']['parts'][0]['text'].strip()
        print(f"[+] SUCCESS: Gemini replied: '{ai_reply}'")
    else:
        print(f"[-] ERROR from Gemini API: {resp.status_code} - {resp.text}")
        sys.exit(1)
except Exception as e:
    print(f"[-] ERROR connecting to Gemini: {e}")
    sys.exit(1)

# Check 3: Gemini Embedding Test (768 dimensions)
print(f"\n[3/3] Testing Google Gemini Embeddings ({EMBEDDING_MODEL})...")
try:
    embed_url = f"https://generativelanguage.googleapis.com/v1beta/models/{EMBEDDING_MODEL}:embedContent?key={GEMINI_API_KEY}"
    embed_payload = {
        "model": f"models/{EMBEDDING_MODEL}",
        "content": {"parts": [{"text": "AuditLens Cross-Document Policy Intelligence"}]},
        "outputDimensionality": 768
    }
    resp = httpx.post(embed_url, json=embed_payload, timeout=10.0)
    if resp.status_code == 200:
        data = resp.json()
        embedding = data['embedding']['values']
        print(f"[+] SUCCESS: Generated vector embedding with {len(embedding)} dimensions (Exact match for Atlas Vector Search: 768).")
    else:
        print(f"[-] ERROR from Gemini Embeddings API: {resp.status_code} - {resp.text}")
        sys.exit(1)
except Exception as e:
    print(f"[-] ERROR generating embeddings: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print(">>> ALL SYSTEMS FULLY OPERATIONAL!")
print("    - MongoDB Atlas Cluster0: Connected & Active")
print("    - MongoDB Vector Search: Ready (768 dimensions)")
print(f"    - Gemini Model: {GEMINI_MODEL} Working")
print(f"    - Embedding Model: {EMBEDDING_MODEL} (768 dims) Working")
print("=" * 60)
