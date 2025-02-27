from abc import ABC,abstractmethod

class parent(ABC):
    @abstractmethod
    def display(self):
        pass

class child(parent):
    def display(self):
        print(" i am implementing this function other wise i will get error since i am an interface(which contains only abstract methods)")
# class relative(parent):
#     def displa(self):
#         pass
# # i will give error because i am not implementing
# r=relative()
# i will give error
c=child()
c.display()


