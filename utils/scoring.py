import numpy as np


def calculate_resume_score(similarity_scores):
    """
    Calculate AI resume score based on semantic similarity.
    """

    if len(similarity_scores) == 0:
        return 0

    # Convert to percentage
    avg_score = np.mean(similarity_scores) * 100

    # Clamp value between 0–100
    final_score = max(0, min(100, avg_score))

    return round(final_score, 2)


def get_readiness_level(score):
    """
    Industry readiness category
    """

    if score >= 80:
        return "🔥 Industry Ready"
    elif score >= 60:
        return "⭐ Strong Candidate"
    elif score >= 40:
        return "⚡ Needs Improvement"
    else:
        return "📘 Beginner Level"