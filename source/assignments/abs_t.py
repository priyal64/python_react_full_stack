from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Dog class implementing make_sound()
class Dog(Animal):
    def make_sound(self):
        print("Bark!")

# Cat class implementing make_sound()
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Creating objects
dog = Dog()
cat = Cat()

# Calling the make_sound() method
dog.make_sound()
cat.make_sound()
