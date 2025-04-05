import cohere, os
from dotenv import load_dotenv
load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def get_cohere_response(prompt):
    response = co.chat(
        model="command-r-plus",
        message=prompt
    )
    return response.text.strip()
