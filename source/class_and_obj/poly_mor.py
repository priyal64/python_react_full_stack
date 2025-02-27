class poly_mor:
    # def __init__(self):
    #     self.message="hello"
    
    def display(self):
        print("i am from poly_mor class")
    
class mor_poly:
    # def __init__(self):
    #     self.message="ok"
    def display(self):
        print("i am from other class")

# for c in [poly_mor(),mor_poly()]:
#     c.display()

c=poly_mor()
c.display()

d=mor_poly()
d.display()