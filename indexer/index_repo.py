import os

from chunker import chunk_text
from embedder import generate_embedding

import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="codebase"
)

repo_path = (
    "data/repositories/test_project"
)

counter = 0

for root, dirs, files in os.walk(
    repo_path
):

    for file in files:

        file_path = os.path.join(
            root,
            file
        )

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as f:

                content = f.read()

            chunks = chunk_text(
                content
            )

            for chunk in chunks:

                vector = generate_embedding(
                    chunk
                )

                collection.add(
                    ids=[str(counter)],
                    documents=[chunk],
                    embeddings=[vector],
                    metadatas=[
                        {
                            "file": file
                        }
                    ]
                )

                counter += 1

        except Exception as e:

            print(
                f"Error: {file}",
                e
            )

print(
    "Indexing Complete!"
)

print(
    "Total Chunks:",
    collection.count()
)