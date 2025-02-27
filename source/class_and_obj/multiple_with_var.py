

class Father():
	father_name = ""
	def father(self):
		print(self.name)

# mother class with attribute mother_name
class Mother():
	mother_name = ""
	def mother(self):
		print(self.name)

# creating derived child class
class Child(Father, Mother):
	def parents(self):
		# Using super() method to access parent classes
		super().__init__()
		print("Father :", self.father_name)
		print("Mother :", self.mother_name)

# creating child object
child = Child()
child.father_name = "papa"
child.mother_name = "mumma"
child.parents()
