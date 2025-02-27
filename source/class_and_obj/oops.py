class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def display_info(self):
        print(f"this car is a {self.brand} {self.model}.")
    
car1=car("TATA","NANO")
car2=car("HYUNDAI","HONDA-CITY")
car1.display_info()
car2.display_info()