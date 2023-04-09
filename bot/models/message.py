from typing import Optional
from dataclasses import dataclass


@dataclass
class Message:
    id: int
    text: str
    author: str
    reply: Optional[int] = None


@dataclass
class Answer:
    text: str
