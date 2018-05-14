# Python strengh is the ability to import modules that add new features
import sys

# you can see arguments on the command line
print(sys.argv)
# get 2nd element of argument array (argument with offset 1), and convert it from text tonumber (integer)
#print(int(sys.argv[1]))

# define a function 
def prime_factors(n):
	# example of for loop 
	# example of if
	# example of remainder of division by an integer
	for i in range(3, n):
		print("i = ", i)
		if i % 2 == 0:
			print(i, "is even")
		if i % 3 == 0:
			print(i, "is multiple of 3")
			
		print("----")
	
	# example of arrays manipulation
	temp = [ 1, 2, 3 ]
	temp.append(5)
	temp.append(6)
	temp[2] = 333
	
	# return result
	return temp
		
#call the function 
res = prime_factors(9)
print("prime factors res:", res)

# TO DO : 
# 1. display divisors of a given number
# 2. append prime factors to an array and return it
# 3 check on 45 (expects 3x3x5), google "while loop"
# 4. take input on command line
