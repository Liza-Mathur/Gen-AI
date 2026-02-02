from email_cleaner import clean_email_text
from email_loader import load_email_from_eml
from llm_subject import generate_subject

def run_pipeline(email_path,openai_client):
    raw_email = load_email_from_eml(email_path)
    clean_email = clean_email_text(raw_email)
    subject = generate_subject(clean_email, openai_client)
    return subject
