import json
from pydantic import TypeAdapter, ValidationError

from llms.gemini import GeminiLLM
from tools import TOOLS
from schema import ToolCall,FinalAnswer

StepResult = TypeAdapter(ToolCall|FinalAnswer)

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

            raw_response = self.llm.generate(messages)
            try:
                step = StepResult.validate_json(raw_response)
            except ValidationError as e:
                raise ValueError(
                    f"LLM returned a response that doesn't match either "
                    f"expected shape (ToolCall or FinalAnswer): {e}"
                )from e

            if isinstance(step,ToolCall):
                tool_name = step.tool
                if tool_name not in TOOLS:
                    raise ValueError(f"Unknown tool: {tool_name}")

                tool = TOOLS[tool_name]

                result = tool(**step.args)

                messages.append(
                    {
                        "role": "assistant",
                        "content":  step.model_dump_json(),
                    }
                )

                messages.append(
                    {
                        "role": "tool",
                        "content": result,
                    }
                )

                continue

            elif isinstance(step, FinalAnswer):
                return step.answer