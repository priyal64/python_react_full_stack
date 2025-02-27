class name:
    def __init__(self,name):
        self.name=name
        print("i am constructor ",self.name," is created ")
    
    def __del__(self):
        # self.name=name
        print("i am destructor ",self.name," is destroyed")
    

obj=name("object")