# single level inheritance:
class parent:
    def __init__(self):
        self.eyecolor="brown"

    def display_parent(self):
        print(" this is parent class .")
    
class child(parent):
    # if i call constructor directly 
    # the attribute error comes and it wont print line no 4
    #  so we use super keyword in childclass
    # in real life (logging)
    def __init__(self):
        super().__init__()
    def display_child(self):
        print(" this is child class ")
    
    
    

ch=child()
ch.display_parent()
ch.display_child()
print(ch.eyecolor)

# we can't do:
# p=parent()
# p.display_child()  will get attribute error