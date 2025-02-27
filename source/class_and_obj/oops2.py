class Employee:
    def __init__(self,name,salary,pf,tax,medical_insurance,rent,petrol):

        self.__name=name
        self.__salary=salary
        self.__pf=pf
        self.__tax=tax
        self.__medical_insurance=medical_insurance
        self.__petrol=petrol
        self.__rent=rent
        
    
    def set_salary(self,salary):
        self.__salary=salary

    def get_salary(self):
        
        return self.__salary+emp.allowance()-emp.deductions()
    
    def allowance(self):
        return self.__rent+self.__petrol
    
    def deductions(self):
        self.__pf=self.__salary*(self.__pf/100)
        self.__tax=self.__salary*self.__tax/100
        self.__medical_insurance=self.__salary*self.__medical_insurance/100
        self.__salary=self.__pf+self.__tax+self.__medical_insurance
        return self.__salary
    
emp=Employee("ABCD",50000,2,5,10,2000,2000)
print("salary before update: ",emp.get_salary())
# emp.set_salary(10000)
# print("after update the salary is: ",emp.get_salary())
