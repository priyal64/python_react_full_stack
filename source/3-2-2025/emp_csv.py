import csv

class Employee:
    # created a static variable 
    
    # file.write()
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


        # row=str(name+","+str(age)+","+role)
        # self.file.writelines(row)



data=["name","age","role"]
# file=open("emp.csv","a",newline="\n")
# file.write(data)
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

with open('emp.csv', 'a') as f:
    # file=open('emp.csv','r') 
    csv_writer = csv.writer(f)
    # c=csv.reader(file)
    # if len(c)==0:
    csv_writer.writerow(data)
    csv_writer.writerows(Employee.main_lis)

with open('emp.csv','r')as f:
    reader=csv.reader(f)
    for r in reader:
        print(r)