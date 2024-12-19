from accessify import private, protected

class Numbers:
    favorite_number = 18
    def __init__(self, number):
        self._number = number

    @private
    @classmethod
    def print_favorite_number(cls):
        return cls.favorite_number


print(Numbers.print_favorite_number())
