#Polymorphism

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)

class Admin(Person):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level

    def level(self):
        print(self.level)

admin1 = Admin("Administrator",18, 1)
admin1.level()


