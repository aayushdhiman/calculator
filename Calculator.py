import os
print "This is a calculator. Please enter your expression seperated by spaces."
x,y,z = input("").split(" ")

def integer(x,z):
	try:
    		x = int(x)
  	except ValueError:
    		print 'The input "'+x+'" is invalid.'
raise SystemExit
#    sys.exit

try:
			z = int(z)
except ValueError:
			print 'The input "'+z+'" is invalid.'
raise SystemExit
def Calculator(x,y,z):
	integer(x,z)
	if y == "*":
		return x*z
	elif y == "/":
		return x/z
	elif y == "+":
		return x+z
	elif y == "-":
		return x-z 

print(Calculator(x,y,z))
