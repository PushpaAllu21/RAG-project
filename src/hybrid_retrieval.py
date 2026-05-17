from rank_bm25 import BM25Okapi
from sentence_transformers import CrossEncoder
import numpy as np
import pickle


reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def hybrid_search(db, query, k=5):

    # Load documents dynamically
    with open("documents.pkl", "rb") as f:
        all_docs = pickle.load(f)

    # BM25 corpus
    corpus = [
        doc.page_content.split()
        for doc in all_docs
    ]

    bm25 = BM25Okapi(corpus)

    # Semantic retrieval
    semantic_docs = db.similarity_search(query, k=k)

    # BM25 retrieval
    tokenized_query = query.split()

    bm25_scores = bm25.get_scores(tokenized_query)

    top_bm25_idx = np.argsort(
        bm25_scores
    )[::-1][:k]

    keyword_docs = [
        all_docs[i]
        for i in top_bm25_idx
    ]

    # Combine results
    combined_docs = semantic_docs + keyword_docs

    unique_docs = []
    seen = set()

    for doc in combined_docs:

        content = doc.page_content

        if content not in seen:
            unique_docs.append(doc)
            seen.add(content)

    # Reranking
    pairs = [
        [query, doc.page_content]
        for doc in unique_docs
    ]

    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(scores, unique_docs),
        key=lambda x: x[0],
        reverse=True
    )

    top_docs = [
        doc
        for score, doc in ranked[:k]
    ]

    return top_docs