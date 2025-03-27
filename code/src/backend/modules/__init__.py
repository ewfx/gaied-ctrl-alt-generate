import os
from dotenv import load_dotenv
from .llm_connector import LLMClient

# Load environment variables from .env file
load_dotenv()

llm_client = LLMClient(
    api_key=os.getenv("GOOGLE_API_KEY"),
    model="gemini-1.5-pro-latest",
    temperature=0.5
)
