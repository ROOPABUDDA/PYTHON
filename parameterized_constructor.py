class Student:
	"""this is a parameterised constructor"""
	def __init__(self,name):
		print("This is parameterised constructor")
		self.name = name
	def show(self):
		print("Hello {}".format(self.name))

student1 = Student()
student1.show("Roopa")