from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def max_speed(self):
        pass

# Car class implementing max_speed()
class Car(Vehicle):
    def max_speed(self):
        return "200 km/h"

# Bike class implementing max_speed()
class Bike(Vehicle):
    def max_speed(self):
        return "150 km/h"

# Creating objects
car = Car("Toyota")
bike = Bike("Yamaha")

# Printing brand and maximum speed
print(f"Car Brand: {car.brand}, Max Speed: {car.max_speed()}")
print(f"Bike Brand: {bike.brand}, Max Speed: {bike.max_speed()}")