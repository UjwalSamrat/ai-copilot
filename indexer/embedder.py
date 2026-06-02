from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Model loaded successfully!")

text = "JWT authentication validation"

vector = model.encode(text)

print("\nEmbedding generated!")

print("Vector Length:", len(vector))

print("First 10 values:")

print(vector[:10])