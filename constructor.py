class ComplexNumber:
	def __init__(self,r=0,i=0):
		self.real = r
		self.image = i
	def getData(self):
		print("{}+{}j".format(self.real,self.image))


c1 =  ComplexNumber(5,6)
c1.getData()
