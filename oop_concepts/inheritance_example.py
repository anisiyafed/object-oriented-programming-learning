# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic sound"

    def info(self):
        return f"{self.name} is a {self.species}."


# Inheritance
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

    def info(self):
        return f"{self.name} is a {self.breed}, which is a type of dog."


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"

    def info(self):
        return f"{self.name} is a {self.color} cat."


generic_animal = Animal("Generic", "Unknown species")
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

print(generic_animal.info())
print(generic_animal.make_sound())
print()

print(dog.info())
print(dog.make_sound())
print()

print(cat.info())
print(cat.make_sound())
