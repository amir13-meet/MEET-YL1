class Integer(object):
	def __init__(self, x, y = True):
		self.y = y
		self.x = x
	def Display(self):
		if (self.y == True):
			print str(self.x)
		else:
			print str(self.x)
	def Add(self, z):
		return self.x + z

	def Subtract(self, z):
		return self.x - z

	def Multiply(self, z):
		return self.x * z

	def Divide(self, z):
		return self.x / z
			

#----------------------------------------------------------------------

class NegativeInteger(Integer):
	def __init__(self, x):
		Integer.__init__(self,x,False)
	def Display(self):
		Integer.Display(self)
		print "This is an object of type NegativeInteger"

#----------------------------------------------------------------------

if __name__ == "__main__":
	#print "Michele"
	#test = Integer(int(raw_input("Enter a positive number: ")))
	#test.Display()
	#print ""
	#test2 = NegativeInteger(int(raw_input("Enter a negative number: ")))
	#test2.Display()
	#A = [test, test2]
	#for i in A:
		#i.Display()
	#B = []
	#x = int(raw_input("How many numbers do you want to create?: "))
	#for i in range (1, x+1):
	#	st = raw_input("'+' or '-' ?: ")
	#	if (st == "+"):
	#		B.append(Integer((int(raw_input("Enter your "+st+ "number: ")), True)))
	#	elif (st == "-"):
	#		B.append(NegativeInteger((int(raw_input("Enter your "+st+ "number: ")), True)))
	#for i in B:
	#	i.Display()
	
	num = Integer(10, True)
	print num.Add(2) #12
	print num.Subtract(7) #3
	print num.Multiply(2) #20
	print num.Divide(2) #5
	
	
			
