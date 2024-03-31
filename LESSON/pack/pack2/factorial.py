#! /usr/bin/python3
def facto():
	n = int(input("Enter number: "))
	mul = 1
	for i in range(1,n+1):
		mul *= i
	print(mul)
