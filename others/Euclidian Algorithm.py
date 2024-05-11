#! /usr/bin/python3

'''
Euclidian Algorithm: It is an algorithm to find greatest common divisor (GCD) of any two numbers.
'''

def gcd(r1:int,r2:int):
	if r1 == 0 or r2 == 0:
		return max(r1, r2)
	elif r1 == 1 or r2 == 1:
		return 1
	else:
		dividend = max(r1,r2)
		divisor = min(r1,r2)
		quotient = dividend // divisor
		remainder = dividend - (quotient * divisor)
		while(True):
			print(dividend, divisor, quotient, remainder)
			dividend = divisor
			divisor = remainder
			if divisor == 0:
				break
			quotient = dividend // divisor
			remainder = dividend - (quotient * divisor)

def multiplicative_inverse(a, b):
	dividend = max(a, b)
	divisor = min(a, b)
	quotient = dividend // divisor
	remainder = dividend - (quotient * divisor)
	t1 = 0
	t2 = 1
	t = t1 - (t2 * quotient)
	while(True):
		print(dividend, divisor, quotient, remainder,t1, t2, t)
		dividend = divisor
		divisor = remainder
		if divisor == 0:
			break
		quotient = dividend // divisor
		remainder = dividend - (quotient * divisor)
		t1 = t2
		t2 = t
		t = t1 - (t2 * quotient)
	return t2


print(multiplicative_inverse(7, 26))
