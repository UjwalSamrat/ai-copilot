import chromadb

from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Model loaded!")

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="codebase"
)

question = input(
    "\nAsk Question: "
)

query_vector = model.encode(
    question
).tolist()

results = collection.query(
    query_embeddings=[query_vector],
    n_results=3
)

print("\nResults:\n")

for i, doc in enumerate(
    results["documents"][0]
):

    print(
        f"\nResult {i+1}:"
    )

    print(doc)

    print(
        "\nMetadata:"
    )

    print(
        results["metadatas"][0][i]
    )