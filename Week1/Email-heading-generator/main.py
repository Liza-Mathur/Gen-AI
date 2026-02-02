from dotenv import load_dotenv
import os
from pipeline import run_pipeline
from openai import OpenAI

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    openai_obj = OpenAI()
    
    email_path = "emails/HindTimes.eml"

    subject = run_pipeline(email_path,openai_obj)

    print("\nSuggested Subject Line:")
    print(subject)


if __name__ == "__main__":
    main()
