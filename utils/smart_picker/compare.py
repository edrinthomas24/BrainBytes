from sklearn.metrics.pairwise import cosine_similarity

def compare_embeddings(prompt_emb, response_emb):
    return float(cosine_similarity([prompt_emb], [response_emb])[0][0])
