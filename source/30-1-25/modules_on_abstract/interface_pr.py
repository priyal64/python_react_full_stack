from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(animal):
    def make_sound(self):
        return "bark!"
c=dog()
print(c.make_sound())
# this example is of interface