from abc import ABC,abstractmethod
class pan:
    @abstractmethod
    def display(self,pan):
        pass

class father(pan):
    def display(self):
        print(" father's pan card is: ","ans123")
    
class child(pan):
    def display(self):
        print(" child's pan card is: ","pqr123")

f=father()
f.display()       
ch=child()
ch.display()