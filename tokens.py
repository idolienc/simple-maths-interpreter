from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    NUMBER = 1
    ADD = 2
    SUBTRACT = 3
    MULTIPLY = 4
    DIVIDE = 5

@dataclass
class Token():
    type: TokenType
    value: str