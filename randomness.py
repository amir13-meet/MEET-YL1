from random import randint

def potato():
	print "Enter n "	
	n = raw_input()
	if (n == "n"):
		x = randint(1,2)
		if (x == 1):
			print "Heads"
		elif (x == 2):
			print "Tails"

if __name__ == "__main__":
	while True:
		potato()
