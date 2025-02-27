class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return 3.14*self.rad*self.rad
    
class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2
    
c=circle(2)
sq=square(4)
print(c.area())
print(sq.area())
        
