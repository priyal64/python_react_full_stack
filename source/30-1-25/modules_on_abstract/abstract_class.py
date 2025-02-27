from abc import ABC,abstractmethod
class father(ABC):
    @abstractmethod
    def display(self):
        pass
    def show(self):
        print(" concrete method") #methods in abstract class is called concrete method if not abstract methods
# class child(father):
#     def display(self):
#         print(" hello i am from child class ")


# ch=child()
# ch.display()
# ch.show()