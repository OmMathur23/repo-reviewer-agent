from google import genai
from src.config import GEMINI_API_KEY, MODEL_NAME

class GeminiLLM:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt:str)->str:
        interaction = self.client.interactions.create(
            model = MODEL_NAME,
            input = prompt
        )
    return interaction.output_text

    
    