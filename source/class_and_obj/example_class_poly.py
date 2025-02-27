class example:
    def __init__(self,name):
        print("helloo ",name,"how old are you ?")
        
    def __init__(self,age):
        print("is of ",age,"years old")
    
obj=example("piyal")
# the above will not print name one constructor
# instead will go to age one
# because of overriding
#  so other examples are:

class example:
    def __init__(self,*args):
        if len(args)==1:
            print("hello ",args[0])
        elif len(args)==2:
            print("hello ",args[0],"is of ",args[1],"years old")

        
obj2=example("priyal",20)
        
# using named variable

class example:
    def __init__(self,**kwargs):
        if "name" in kwargs and "age" in kwargs:
            print("hello ",kwargs['name'],"is of ",kwargs['age'],"years old")
        elif "name" in kwargs:
            print("hello ,",kwargs['name'])
        self.x=kwargs['name']
    # x=kwargs['name'] this can't be used out of constructor or this function  therefore we are supposed to assign this value with self then this value can be accessed in whole code



obj3=example(name="pppp",age=22)
# print(obj3.age) this will give error
print(obj3.x)
