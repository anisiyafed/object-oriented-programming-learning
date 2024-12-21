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

animals = [Dog(), Cat(), Bird()]

print("Animal sounds:")
for animal in animals:
    print(animal.make_sound())

