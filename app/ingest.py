import os
import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="zepto_support"
)

docs_folder = "docs"

for filename in os.listdir(docs_folder):

    path = os.path.join(
        docs_folder,
        filename
    )

    with open(path,"r",encoding="utf-8") as f:
        text = f.read()

    embedding = model.encode(
        text
    ).tolist()

    collection.add(
        ids=[filename],
        documents=[text],
        embeddings=[embedding]
    )

print("Loaded documents.")