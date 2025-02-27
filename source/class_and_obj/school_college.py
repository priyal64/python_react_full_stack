class school:
    def __init__(self):
        self.name=input("enter name: ")
        self.address=input("enter address: ")
        self.x_marks=int(input("enter marks: "))

    def display(self):
        print(" name of the student: ",self.name)
        print(" student's class 10th marks: ",self.x_marks)

class higher_edu(school):
    def science(self):
        print(" is in science course ")
    
    def commerce(self):
        print("is in commerce course")

s=higher_edu()
str=int(input("enter 1 for science 2 for commerce"))
if str==1:
    s.science()
else:
    s.commerce()
    