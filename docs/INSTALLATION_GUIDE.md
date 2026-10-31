# Installation & Deployment Guide: AuditLens AI
**UNCHARTED 2026 | Track 2: RAG Engine**  
**Team Elite (SVNIT Surat): Rishit Modh, Bhavya Juneja, Sugandh Jha**

---

## 1. System Prerequisites

Before running AuditLens AI locally or deploying to the cloud, ensure your system meets the following requirements:
- **Operating System:** Linux, macOS, or Windows 10/11
- **Python Version:** Python 3.10, 3.11, or 3.12 (Python 3.14 compatible)
- **MongoDB Atlas Cluster:** An active MongoDB Atlas account (Free M0 tier on AWS is fully sufficient)
- **Google Gemini API Key:** A free API key from [Google AI Studio](https://aistudio.google.com/)
- **Hardware Memory:** Minimum 4 GB RAM (8 GB recommended for local embedding computation)

---

## 2. Environment Variables Configuration

Copy `.env.example` to create your local `.env` file:

```bash
cp .env.example .env
```

Populate the required environment variables:

```ini
# ==========================================
# MongoDB Atlas Configuration
# ==========================================
# Replace with your Atlas connection URI (include username & password)
MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
DATABASE_NAME=auditlens_db
COLLECTION_NAME=documents

# ==========================================
# Google Gemini API Configuration
# ==========================================
GEMINI_API_KEY=your_gemini_api_key_here

# ==========================================
# Server Configuration (Optional Defaults)
# ==========================================
PORT=8000
HOST=0.0.0.0
ENVIRONMENT=production
```

> [!CAUTION]
> Never commit your `.env` file or expose your MongoDB connection string or Gemini API key to version control.

---

## 3. MongoDB Atlas Vector Search Index Setup

1. Log in to the [MongoDB Atlas Console](https://cloud.mongodb.com/).
2. Select your cluster (e.g. `Cluster0`) and navigate to **"Atlas Search & Vector Search"**.
3. Click **"Create Search Index"** and select **"Atlas Vector Search (JSON Editor)"**.
4. Select database `auditlens_db` and collection `documents`.
5. Set the **Index Name** to: `vector_index`.
6. Paste the following JSON definition:

```json
{
  "fields": [
    {
      "type": "vector",
      "path": "embedding",
      "numDimensions": 768,
      "similarity": "cosine"
    },
    {
      "type": "filter",
      "path": "doc_id"
    },
    {
      "type": "filter",
      "path": "category"
    }
  ]
}
```
7. Click **"Save & Build"**. Wait ~1 minute until the index status transitions to `Active`.

---

## 4. Local Installation Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/rishitmodh12/AuditLens.AI.git
cd AuditLens.AI
```

### Step 2: Create and Activate a Virtual Environment
**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Required Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Seed Sample Enterprise Contracts into Atlas
Populate the 3 core Indian enterprise reference contracts into MongoDB Atlas:
```bash
python -m backend.sample_data
```
*Expected Output:*
```text
Connecting to MongoDB Atlas: auditlens_db ...
Cleared 12 existing chunks.
Seeding Customer_Enterprise_SLA_2026.pdf ...
Seeding Internal_Security_Incident_Policy_v4.pdf ...
Seeding Cloud_Vendor_Master_Services_Agreement.pdf ...
Successfully seeded 3 documents (12 vector chunks) into Atlas!
```

### Step 5: Start the Development Server
```bash
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload
```

Open your browser and navigate to:  
`http://127.0.0.1:8000`

---

## 5. Verification Commands

Run these quick automated tests to confirm that your local environment is functioning correctly:

### Test 1: Health Endpoint Check
```bash
curl -s http://127.0.0.1:8000/api/health
```
*Expected Response:*
```json
{"status":"healthy","database":"auditlens_db","mongodb_connected":true,"indexed_documents_count":3,"total_vector_chunks":12}
```

### Test 2: Run Evaluation Benchmark
```bash
curl -s http://127.0.0.1:8000/api/evaluate
```
*Expected Response:*
```json
{"recall_at_1": 1.0, "recall_at_3": 1.0, "refusal_accuracy": 1.0, "total_test_queries": 8}
```

---

## 6. Docker & Production Deployment (Render)

AuditLens AI is containerized for seamless cloud deployment on Render, Fly.io, or AWS.

### Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose port
EXPOSE 8000

# Start server
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Deploying to Render
1. Create a **New Web Service** connected to your GitHub repository `https://github.com/rishitmodh12/AuditLens.AI`.
2. Set Environment to **Python** (or **Docker**).
3. Set Build Command: `pip install -r requirements.txt`.
4. Set Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`.
5. Under **Environment Variables**, add:
   - `MONGODB_URI`: Your Atlas connection string.
   - `GEMINI_API_KEY`: Your Google Gemini API key.
   - `DATABASE_NAME`: `auditlens_db`.
6. Click **Deploy Web Service**.
