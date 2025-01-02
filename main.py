from dataclasses import dataclass

@dataclass
class Things:
    name: str
    weight: float
    amount: int

    def __eq__(self, other):
        if self.name == other.name:
            return self.weight == other.weight
        else:
            return "We need the same things!"

@dataclass
class PC(Things):
    model: str
    description: str
    price = 0

acer = PC("Acer 22", "maybe cool pc", "22", "some description", 12222)

print(acer.__dict__)