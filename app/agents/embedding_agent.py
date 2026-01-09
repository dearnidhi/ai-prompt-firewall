# app/agents/embedding_agent.py

import json
from app.models.embedding_model import load_embedding_model
from app.utils.similarity import compute_similarity
from app.config import EMBEDDING_SCORE, JAILBREAK_DATASET

model = load_embedding_model()

with open(JAILBREAK_DATASET, "r") as f:
    jailbreak_data = json.load(f)

jailbreak_prompts = [item["prompt"] for item in jailbreak_data]
jailbreak_embeddings = model.encode(jailbreak_prompts)

def embedding_check(prompt: str):
    prompt_embedding = model.encode(prompt)

    max_similarity = 0.0
    matched_prompt = ""

    for i, jb_embedding in enumerate(jailbreak_embeddings):
        similarity = compute_similarity(prompt_embedding, jb_embedding)

        if similarity > max_similarity:
            max_similarity = similarity
            matched_prompt = jailbreak_prompts[i]

    if max_similarity > 0.75:
        return EMBEDDING_SCORE, f"Semantic jailbreak detected (similar to: '{matched_prompt}')"

    return 0.0, ""
