class Сharacter:
    MIN_HEALTH = 0
    MAX_HEALTH = 100
    USER_HEALTH = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def bite(cls, damage):
        cls.USER_HEALTH -= damage
        if cls.USER_HEALTH <= 0:
            return "You're dead"
        else:
            return cls.USER_HEALTH

    @staticmethod
    def say_word(word):
        return word

    
ugo = Сharacter("Ugo", 25)
print(Сharacter.say_word("UgoGa"))