#!/usr/bin/python3
def factorial(n):
	if  n == 0:
		return 1
	else:
		return n * factorial(n-1)

n = int(input('Enter the value to calculate the factorial: '))
print("The factorial of a given number is ", factorial(n))