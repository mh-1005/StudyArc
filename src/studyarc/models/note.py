from dataclasses import dataclass


@dataclass
class Note:
    title: str
    subject: str
    content: str
    id: int | None = None
