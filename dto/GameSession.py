from dataclasses import dataclass


@dataclass
class GameSession:
    id: int
    target_word: str
