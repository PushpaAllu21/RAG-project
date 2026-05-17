from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import pickle


def create_vector_store(documents):

    embedding = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(documents, embedding)

    db.save_local("embeddings/")

    with open("documents.pkl", "wb") as f:
        pickle.dump(documents, f)

    return db
