import json

from llms.gemini import GeminiLLM
from tools import TOOLS


SYSTEM_PROMPT = """
You are an AI software architect.

Available tools:

1. read_file(path: str)

When you need a tool, respond ONLY with JSON:

{
    "type": "tool",
    "tool": "<tool_name>",
    "args": {
        ...
    }
}

When you have the final answer, respond ONLY with JSON:

{
    "type": "final",
    "answer": "..."
}

Never output markdown.
Never output explanations.
Only output valid JSON.
"""


class Agent:
    def __init__(self):
        self.llm = GeminiLLM()

    def run(self, user_prompt: str):

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]

        while True:

            response = self.llm.generate(messages)
            response = json.loads(response)

            if response["type"] == "tool":

                tool_name = response["tool"]

                if tool_name not in TOOLS:
                    raise ValueError(f"Unknown tool: {tool_name}")

                tool = TOOLS[tool_name]

                result = tool(**response["args"])

                messages.append(
                    {
                        "role": "assistant",
                        "content": json.dumps(response),
                    }
                )

                messages.append(
                    {
                        "role": "tool",
                        "content": result,
                    }
                )

                continue

            elif response["type"] == "final":
                return response["answer"]