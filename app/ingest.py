from pathlib import Path
import chromadb

# Create Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection if it doesn't exist
collection = client.get_or_create_collection(
    name="zepto_docs"
)


def ingest_documents():

    existing = collection.count()

    if existing > 0:
        print(f"Collection already contains {existing} documents.")
        return

    docs_folder = Path("docs")

    if not docs_folder.exists():
        print("Docs folder not found.")
        return

    for file in docs_folder.glob("*.txt"):

        content = file.read_text(
            encoding="utf-8"
        )

        collection.add(
            ids=[file.stem],
            documents=[content],
            metadatas=[
                {"source": file.name}
            ]
        )

        print(f"Added: {file.name}")

    print(
        f"Ingestion complete. Total documents: {collection.count()}"
    )


if __name__ == "__main__":
    ingest_documents()
