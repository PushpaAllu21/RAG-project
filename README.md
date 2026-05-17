# RAG Project

A Retrieval-Augmented Generation (RAG) application built with LangChain, OpenAI, FAISS, and Streamlit for document processing and Q&A.

## Features

- Document ingestion and preprocessing
- Text chunking with overlap
- Vector embeddings using FAISS
- Retrieval-Augmented Generation pipeline
- Streamlit web interface
- MLflow experiment tracking

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PushpaAllu21/RAG-project.git
   cd RAG-project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (e.g., OpenAI API key) in a `.env` file.

## Usage

### Run the Streamlit App
```bash
streamlit run app/streamlit_app.py
```

### Run the Main Pipeline
```bash
python main_pipeline/main.py
```

### Track Experiments with MLflow
```bash
python MLflow/mlflow_tracking.py
```

## Project Structure

- `app/`: Streamlit application
- `embeddings/`: FAISS index storage
- `main_pipeline/`: Core pipeline execution
- `MLflow/`: Experiment tracking
- `src/`: Source modules (embedding, ingestion, preprocessing, RAG pipeline, retrieval)

## Requirements

- Python 3.8+
- OpenAI API key
- Dependencies listed in `requirements.txt`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License