import re

def clean_text(text):
    # convert to lowercase
    text = text.lower()

    # remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text
