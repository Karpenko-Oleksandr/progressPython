class Person:
    name = ''
    age = ''
    
    def greeting(self):
        print(f'Hi, my name is {self.name}!')

    
person1 = Person()

nameOfPerson1 = input('Hello, what\'s your name?: ')
person1.name = nameOfPerson1

person1.greeting()