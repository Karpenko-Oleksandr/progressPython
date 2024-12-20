class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property   
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        print("Deleted")
    
p = Person("Person", 33)
p.age = 34
print(p.age, p.__dict__)
del p.age