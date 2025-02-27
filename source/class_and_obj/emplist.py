class Employee:
    # created a static variable
    main_lis=[]   
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
        self.lis=[name,age,role]
        Employee.main_lis.append(self.lis)
        # self.name=input("enter name of the employee: ")
        # self.age=int(input("enter the age of the person: "))
        # self.role=input("enter the role of employee: ")
li=["NAME","AGE","ROLE"]
Employee.main_lis.append(li)
print(Employee.main_lis)

while(True):
    # adding lists
    n=int(input("enter 1 for input 2 for stop: "))
    if n==1:
        name=input("enter the name of the person: ")
        age=int(input("enter age of the person: "))
        role=input("enter role of the person: ")
        obj=Employee(name,age,role)
    else:
        break

for x in Employee.main_lis:
    print (x)

    