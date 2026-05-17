import streamlit as st
from src.ingestion import fetch_papers
from src.preprocessing import chunk_data
from src.embedding import create_vector_store
from src.hybrid_retrieval import hybrid_search
from src.comparitive_analysis import compare_papers


st.set_page_config(
    page_title="Pharma RAG Research Assistant",
    layout="wide"
)


st.title("Biomedical Research RAG Assistant")

st.markdown("""
This AI system:
- Fetches PubMed papers
- Creates embeddings
- Performs hybrid retrieval
- Generates comparative biomedical analysis
- Shows source-grounded evidence
""")


# Sidebar
st.sidebar.header("Settings")

paper_limit = st.sidebar.slider(
    "Number of Papers",
    min_value=3,
    max_value=20,
    value=5
)


# Main Inputs
research_query = st.text_input(
    "Research Topic",
    value="PARP inhibitors AND cancer AND DNA repair"
)

user_question = st.text_area(
    "Ask Biomedical Question",
    value="Compare PARP inhibitor outcomes in BRCA mutated cancers"
)


if st.button("Run RAG Pipeline"):

    with st.spinner("Fetching PubMed papers..."):
        papers = fetch_papers(research_query, limit=paper_limit)

    if not papers:
        st.error("No papers fetched.")
        st.stop()

    st.success(f"Fetched {len(papers)} papers")


    # Show papers
    st.subheader("Fetched Papers")

    for idx, paper in enumerate(papers, start=1):
        with st.expander(f"Paper {idx}: {paper['title']}"):
            st.write(f"PMID: {paper['pmid']}")
            st.write(f"Journal: {paper['journal']}")
            st.write(f"Year: {paper['year']}")
            st.write(f"URL: {paper['url']}")


    # Chunking
    with st.spinner("Chunking documents..."):
        docs = chunk_data(papers)

    st.info(f"Created {len(docs)} chunks")


    # Embeddings
    with st.spinner("Creating embeddings + vector DB..."):
        db = create_vector_store(docs)

    st.success("Embeddings created successfully")


    # Retrieval
    with st.spinner("Running hybrid retrieval..."):
        retrieved_docs = hybrid_search(db, user_question)


    st.subheader("Retrieved Evidence")

    for idx, doc in enumerate(retrieved_docs, start=1):
        with st.expander(f"Retrieved Chunk {idx}"):
            st.write(f"PMID: {doc.metadata.get('pmid')}")
            st.write(f"Title: {doc.metadata.get('title')}")
            st.write(doc.page_content)


    # Comparative Analysis
    with st.spinner("Generating comparative analysis..."):
        answer = compare_papers(user_question, retrieved_docs)


    st.subheader("AI Comparative Analysis")

    st.write(answer)
