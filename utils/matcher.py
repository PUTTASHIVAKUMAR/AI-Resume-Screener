import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_to_jobs(cleaned_resume_text):

    # Load job roles dataset
    df = pd.read_csv("data/job_roles.csv")

    # Combine resume + job skills
    documents = [cleaned_resume_text] + df["skills"].tolist()

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Resume vector
    resume_vector = tfidf_matrix[0]

    # Job vectors
    job_vectors = tfidf_matrix[1:]

    # Similarity scores
    similarity_scores = cosine_similarity(resume_vector, job_vectors)[0]

    # Add scores to dataframe
    df["score"] = similarity_scores

    # Sort top matches
    top_matches = df.sort_values(by="score", ascending=False).head(3)

    return top_matches
