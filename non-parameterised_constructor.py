class Student:
	"""this is a parameterised constructor"""
	def __init__(self):
		print("This is non parameterised constructor")
	def show(self,name):
		print("Hello {}".format(name))

student1 = Student()
student1.show("Roopa")