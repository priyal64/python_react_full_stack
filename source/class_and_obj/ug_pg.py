class school:
    def __init__(self):
        self.name=input("enter name: ")
        self.address=input("enter address: ")
        self.x_marks=int(input("enter marks: "))

    def display(self):
        print(" name of the student: ",self.name)
        print(" student's class 10th marks: ",self.x_marks)

class higher_edu(school):
    def undergrad(self):
        self.hod=input("enter your hod name: ")
        self.course=input("enter your course name: ")
        self.u_marks=float(input("enter your marks in undergrad:"))
    def display_grad(self):
        print("your course and marks in undergrad: ",self.u_marks,self.course)

    

    
    def postgrad(self):
        self.hod_1=input("enter your hod name: ")
        self.course_1=input("enter your course name: ")
        self.p_marks=float(input("enter your marks in postgrad:"))
    def display_post(self):
        print("your course and marks in postgrad: ",self.p_marks,self.course_1)

s=higher_edu()
s.undergrad()

s.display_grad()
s.postgrad()
s.display_post()
