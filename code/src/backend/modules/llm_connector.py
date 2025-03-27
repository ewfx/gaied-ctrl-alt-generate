import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
import json
import re
from config.prompt_config import PROMPT  # Import the prompt

class LLMClient:
    def __init__(self, api_key: str, model: str, temperature: float):
        genai.configure(api_key=api_key)
        self.llm = ChatGoogleGenerativeAI(
            model=model,
            temperature=temperature,
            google_api_key=api_key
        )
        self.prompt = PROMPT

    def classify_email_and_extract_details(self, message: str) -> dict:
        """
        Process the email content (and attachment content if provided)
        to determine whether it is an enquiry or a loan request.
        If a loan request, extract the loan request type, sub-request type,
        and the loan amount.
        """

        # Define prompt for LLM.
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content=self.prompt),
            HumanMessage(content=message)
        ])

        formatted_prompt = prompt.format()

        # Generate response
        try:
            response = self.llm.invoke(formatted_prompt)
            raw_response = response.content
            cleaned_response = re.sub(r"^```json\n|\n```$", "", raw_response.strip())
            result = json.loads(cleaned_response)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error: LLM response is not valid JSON. Raw response: {cleaned_response}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}")

        return result