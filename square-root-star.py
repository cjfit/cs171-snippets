# basic recursive square root star function for placement exam
# The Star Square Root is the number of times you need to take a square root before the result is less than 2

import math
count = 0
def sqrt_star(n, count=0):
    if (n >= 2):
        return sqrt_star(math.sqrt(n), count+1)
    else:
        return count
if __name__ =='__main__':
	print(sqrt_star(1000)) #Prints 4
	print(sqrt_star(10000)) #Prints 4
	print(sqrt_star(100000)) #Prints 5
