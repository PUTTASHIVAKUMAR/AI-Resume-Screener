import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from models.sentence_model import get_embeddings


def semantic_match(resume_text, job_descriptions, top_n=3):
    """
    Semantic matching using Sentence Transformers
    """

    # Combine resume + jobs
    all_texts = [resume_text] + job_descriptions

    # Convert to embeddings
    embeddings = get_embeddings(all_texts)

    # Resume embedding
    resume_embedding = embeddings[0].reshape(1, -1)

    # Job embeddings
    job_embeddings = embeddings[1:]

    # Calculate similarity
    scores = cosine_similarity(resume_embedding, job_embeddings)[0]

    # Get top matches
    top_indices = np.argsort(scores)[::-1][:top_n]

    results = [(i, scores[i]) for i in top_indices]

    return results