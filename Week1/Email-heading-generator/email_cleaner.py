import re

def clean_email_text(text):
    text = re.sub(r"http\S+", "", text)       # remove links
    text = re.sub(r"\s+", " ", text)          # normalize spaces
    text = text.strip()
    return text
