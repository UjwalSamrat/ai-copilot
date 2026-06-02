import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="codebase"
)

print("Collection Created!")

print(
    "Documents Stored:",
    collection.count()
)