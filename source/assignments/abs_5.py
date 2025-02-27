from abc import ABC, abstractmethod

# Abstract class Person
class Person(ABC):
    @abstractmethod
    def get_name(self):
        pass

# Abstract class Employee
class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

# Manager class inheriting both Person and Employee
class Manager(Person, Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

manager = Manager("piiiii", 100000)
print(f"Name: {manager.get_name()}")
print(f"Salary: {manager.get_salary()}")
