import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="zepto_docs"
)


def retrieve(question: str):

    if collection.count() == 0:
        return (
            "No documents available.",
            "No source"
        )

    results = collection.query(
        query_texts=[question],
        n_results=1
    )

    document = results["documents"][0][0]
    source = results["metadatas"][0][0]["source"]

    return document, source
