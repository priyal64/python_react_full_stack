# creating static class
class class_a:
    def __init__(self):
        self.message="this is class constructor"
    def calculate(self,x,y):
        return x+y
    @staticmethod
    def display():
        print("this is static class ")
    

class_a.display()
# print(class_a.calculate(5,7))
obj=class_a()
print(obj.calculate(2,3))
print(obj.message)

