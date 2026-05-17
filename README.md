# Research Assistant using RAG

An AI-powered literature assistant that retrieves scientific papers from PubMed and generates evidence-based answers using Retrieval-Augmented Generation (RAG), hybrid retrieval, and LLM-powered comparative analysis.

---

# Features

- PubMed paper ingestion
- Biomedical document chunking
- Semantic embeddings using Hugging Face
- FAISS vector database
- Hybrid retrieval:
  - Semantic Search
  - BM25 Keyword Retrieval
  - Cross-Encoder Reranking
- Source-grounded answers with PMIDs
- Comparative multi-paper analysis
- Streamlit interactive UI
- Biomedical literature intelligence pipeline

---

# Tech Stack

- Python
- LangChain
- HuggingFace Embeddings
- FAISS
- BM25
- Streamlit
- Groq API
- PubMed API
- NLP / RAG Architecture

---

# Project Architecture

```text
User Query
    ↓
PubMed Paper Fetching
    ↓
Document Chunking
    ↓
Embedding Generation
    ↓
FAISS Vector Database
    ↓
Hybrid Retrieval
(Semantic + BM25 + Reranking)
    ↓
Source-Grounded Retrieval
    ↓
Comparative Biomedical Analysis
    ↓
LLM Generated Answer
```

---

# Project Structure

```text
RAGproject/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── ingestion.py
│   ├── preprocessing.py
│   ├── embedding.py
│   ├── hybrid_retrieval.py
│   ├── comparative_analysis.py
│   ├── rag_pipeline.py
│   └── main.py
│
├── embeddings/
├── documents.pkl
├── requirements.txt
└── .env
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd RAGproject
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# Install Dependencies

```bash
python -m pip install \
langchain \
langchain-core \
langchain-community \
langchain-text-splitters \
sentence-transformers \
faiss-cpu \
rank-bm25 \
streamlit \
groq \
python-dotenv
```

---

# Environment Variables

Create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

Get API key from:

https://console.groq.com

---

# Run Streamlit App

```bash
python -m streamlit run app/streamlit_app.py
```

---

# Example Queries

## Research Topic

```text
PARP inhibitors AND cancer AND DNA repair
```

## Biomedical Question

```text
Compare PARP inhibitor outcomes in BRCA mutated cancers
```

---

# Key Features Explained

## Hybrid Retrieval

Combines:
- Semantic Vector Search
- BM25 Keyword Search
- Cross-Encoder Reranking

Improves retrieval accuracy for biomedical terminology.

---

## Source-Grounded Answers

Generated responses include:
- PMID references
- retrieved evidence
- paper metadata

Improves explainability and trustworthiness.

---

## Comparative Analysis

The system can:
- compare multiple studies
- identify similarities
- identify contradictions
- summarize mechanisms
- synthesize biomedical findings

---

# Future Improvements

- Regulatory guideline ingestion
- Pharmacovigilance analysis
- Clinical trial protocol analysis
- Knowledge graph integration
- RAG evaluation metrics
- PDF ingestion
- Multi-agent biomedical AI system

---

# Example Output

```text
PARP inhibitors impair DNA repair mechanisms by
blocking single-strand break repair pathways.

Studies suggest improved progression-free survival
in BRCA-mutated ovarian cancer patients.

Sources:
PMID: 123456
PMID: 789101
```

---

# Learning Outcomes

This project demonstrates:
- Retrieval-Augmented Generation (RAG)
- Hybrid Retrieval Systems
- Biomedical NLP
- Vector Databases
- LLM Integration
- Streamlit Deployment
- Evidence-Grounded AI Systems

---

# Author

Pushpa Allu