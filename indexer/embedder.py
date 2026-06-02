from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Model loaded successfully!")

from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

print("Model loaded!")

def generate_embedding(text):

    return model.encode(
        text
    ).tolist()