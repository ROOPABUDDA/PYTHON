class Student:
	def __init__(self,rollno,name):
		self.rollno = rollno
		self.name = name
	def displayStudent(self):
		print('rollno: {}'.format(self.rollno))
		print('name: {}'.format(self.name))


student1 = Student(111,"Anu")
student2 = Student(112,"Banu")

student1.displayStudent()
student2.displayStudent()