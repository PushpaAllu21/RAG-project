import mlflow

mlflow.set_experiment("RAG Research Assistant")

user_q = "test question"
retrieved = ["doc1", "doc2"]
answer = "sample answer"

with mlflow.start_run():
    mlflow.log_param("query", user_q)
    mlflow.log_param("num_docs", len(retrieved))

    mlflow.log_text(answer, "output.txt")