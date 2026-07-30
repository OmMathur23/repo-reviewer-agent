from typing import Any, Literal

from pydantic import BaseModel


class ToolCall(BaseModel):
    type: Literal["tool"]
    tool: str
    args: dict[str, Any]


class FinalAnswer(BaseModel):
    type: Literal["final"]
    answer: str

"""ToolCall — represents "the agent wants to use a tool":

type: Literal["tool"] — a fixed tag that's always exactly the string "tool". This is the discriminator: it's what lets code (or Pydantic itself) tell which variant it's looking at.
tool: str — the name of the tool to call, e.g. "read_file" or "clone_repo".
args: dict[str, Any] — whatever arguments that tool needs, as a flexible key-value dict (e.g. {"path": "README.md"}). Any because different tools take different argument shapes, so it can't be typed more strictly here.

FinalAnswer — represents "the agent is done and has an answer":

type: Literal["final"] — the discriminator, always "final".
answer: str — the actual text response to give the user.
"""