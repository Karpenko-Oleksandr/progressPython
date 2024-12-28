from dataclasses import dataclass

@dataclass
class Things:
    name: str
    weight: float
    amount: int

tg = Things("PC", 3.4, 1)
print(tg)