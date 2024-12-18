class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

test_person = Person("Stephen", 35)
del p.old
test_person.old = 25
print(test_person.old)