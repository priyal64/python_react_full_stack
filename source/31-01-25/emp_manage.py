from abc import ABC, abstractmethod
from typing import List

# Step 1: Define Employee interface using Abstract Base Class (ABC)
class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        pass


# Step 2: Create concrete classes for different types of employees

class Manager(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is managing the team."

    def get_salary(self) -> float:
        return self.salary


class Developer(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is writing code."

    def get_salary(self) -> float:
        return self.salary


class Intern(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is learning and assisting."

    def get_salary(self) -> float:
        return self.salary


# Step 3: Define Department class that manages Employees

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired.")

    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")

    def promote(self, employee: Employee) -> None:
        for i, emp in enumerate(self.employees):
            if emp == employee:
                new_name = "Senior " + emp.name  # Append "Senior" to the name
                
                if isinstance(emp, Intern):
                    promoted_employee = Developer(new_name, emp.get_salary() + 5000)
                    print(f"{emp.name} is promoted to Developer role!")
                elif isinstance(emp, Developer):
                    promoted_employee = Manager(new_name, emp.get_salary() + 10000)
                    print(f"{emp.name} is promoted to Manager role!")
                else:
                    print(f"{emp.name} cannot be promoted further.")
                    return
                
                self.employees[i] = promoted_employee  # Replace with promoted employee
                return
        
        print("Employee not found in the department.")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")


class Security(Employee):
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def work(self) -> str:
        return f"{self.name} is Securing the assets."

    def get_salary(self) -> float:
        return self.salary
    
# Step 4: Create department and add employees

# # Create employees
# manager = Manager("Alice", 80000)
# developer = Developer("Bob", 60000)
# intern = Intern("Charlie", 20000)
# securitystaff=Security("Ram",5000)
m=Manager("manager",90000)
p=Intern("ppp",90909)
# Create a department and hire employees
obj = Department("Tech")


obj.hire(p)

# obj.hire(developer)
# obj.hire(intern)
# obj.hire(securitystaff)
# Show employee details
obj.promote(p)
obj.show_employee_details()

# Total salary in the department
total_salary = obj.get_total_salary()
print(f"Total salary expense for {obj.name} department: ${total_salary}")

