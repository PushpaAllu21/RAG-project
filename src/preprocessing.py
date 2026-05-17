from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_data(papers):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = []

    for paper in papers:
        chunks = splitter.split_text(paper["abstract"])

        for chunk in chunks:
            doc = Document(
                page_content=chunk,
                metadata={
                    "pmid": paper["pmid"],
                    "title": paper["title"],
                    "journal": paper["journal"],
                    "year": paper["year"],
                    "url": paper["url"]
                }
            )

            documents.append(doc)

    return documents
