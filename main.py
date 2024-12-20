class Person:
    def __new__(cls, *args):
        print("Hi, I'm a person!")
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __del__(self):
        print("deleted")

    
p = Person("Person", 33)

p.name = "First_Person"
print(p.name)