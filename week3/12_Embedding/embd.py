import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer

# Calculate how similar two vectors are
def cosine_similarity(a, b):
    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

# Load a pre-trained model that converts text into embeddings
model = SentenceTransformer("all-MiniLM-L6-v2") #384
text = "Machine learning is fun."

# Convert text into an embedding
# embedding=model.encode(text)
# print(embedding.shape)
# print(embedding)

# Two sentences we want to compare
t1 = "There are 24 paid leaves"
t2 = "Cat is wild animal"

# Convert both sentences into embeddings
v1 = model.encode(t1)
v2 = model.encode(t2)


print(cosine_similarity(v1, v2))