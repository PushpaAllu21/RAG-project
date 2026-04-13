import warnings
warnings.filterwarnings("ignore")
from src.ingestion import fetch_papers
from src.preprocessing import chunk_data
from src.embedding import create_vector_store
from src.retrieval import retrieve_docs
from src.rag_pipeline import generate_answer

query ="PARP inhibitors AND cancer AND DNA repair"

# Step 1: Fetch
papers = fetch_papers(query)

# Step 2: Process
texts = [p["abstract"] for p in papers]
docs = chunk_data(texts)
if not papers:
    print("No papers fetched. Try again later.")
    exit()

# Step 3: Embed
db = create_vector_store(docs)

# Step 4: Query
user_q = "How do PARP inhibitors work?"
retrieved = retrieve_docs(db, user_q)

# Step 5: Generate
answer = generate_answer(user_q, retrieved)

print(answer)
print("QUERY:", query)
print("PAPERS:", papers)