class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Bird(Animal):
    def make_sound(self):
        return "Tweet! Tweet!"


def animal_sounds(animals: Animal):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Bird()]

print("Animal sounds:")
animal_sounds(animals)
