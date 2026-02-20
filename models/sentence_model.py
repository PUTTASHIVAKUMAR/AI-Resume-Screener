from sentence_transformers import SentenceTransformer

# Load once (industry practice)
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(text_list):
    """
    Convert text into semantic embeddings
    """
    return model.encode(text_list)