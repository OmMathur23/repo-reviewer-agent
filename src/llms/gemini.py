from google import genai
from google.genai import errors as genai_errors
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from config import GEMINI_API_KEY, MODEL_NAME


class GeminiLLM:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=8),
        retry=retry_if_exception_type(genai_errors.APIError),
        reraise=True,
    )
    def generate(self, messages: list[dict]) -> str:
        parts = []

        for message in messages:
            parts.append(
                f"{message['role'].upper()}:\n{message['content']}"
            )

        prompt = "\n\n".join(parts)

        interaction = self.client.interactions.create(
            model=MODEL_NAME,
            input=prompt,
        )

        return interaction.output_text