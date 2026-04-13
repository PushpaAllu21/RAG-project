import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from src.ingestion import fetch_papers
from src.preprocessing import chunk_data
from src.embedding import create_vector_store
from src.retrieval import retrieve_docs
from src.rag_pipeline import generate_answer

st.set_page_config(page_title="RAG Research Assistant", layout="wide")

st.title("🧠 Research Assistant (RAG)")
st.write("Ask questions from research papers (PubMed powered)")

# ✅ Cache API
@st.cache_data
def cached_fetch(query):
    return fetch_papers(query)

# ✅ Cache embeddings
@st.cache_resource
def cached_vector_store(docs):
    return create_vector_store(docs)

query = st.text_input("Enter your research question:")

if query and query.strip():
    with st.spinner("Fetching and analyzing papers..."):
        
        papers = cached_fetch(query)

        if not papers:
            st.error("❌ No papers found")
            st.stop()

        texts = [p["abstract"] for p in papers]
        docs = chunk_data(texts)

        db = cached_vector_store(docs)

        retrieved = retrieve_docs(db, query)

        answer = generate_answer(query, retrieved)

    st.subheader("📌 Answer")
    st.write(answer)


    st.subheader("📄 Sources")
    for p in papers:
        st.markdown(f"- [{p['title']}]({p['url']})")

    # ✅ Debug view (optional)
    st.subheader("🔍 Retrieved Context")
    for d in retrieved:
        st.write(d.page_content[:300])