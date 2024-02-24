#! /usr/bin/python3
'''

Bitwise Operator: -
----------------

AND          &
OR           |
NOT          ~
XOR          ^
RIGHT-SHIFT  >>
LEFT-SHIFT   <<

Boolean Table: -
-------------
AND Table: -
---------
|-------|-------|-------|
|	X	|	Y	| X & Y |
|-------|-------|-------|
|	0	|	0	|	0	|
|-------|-------|-------|
|	0	|	1	|	0	|
|-------|-------|-------|
|	1	|	0	|	0	|
|-------|-------|-------|
|	1	|	1	|	1	|
|-------|-------|-------|

OR Table: -
--------
|-------|-------|-------|
|	X	|	Y	| X | Y |
|-------|-------|-------|
|	0	|	0	|	0	|
|-------|-------|-------|
|	0	|	1	|	1	|
|-------|-------|-------|
|	1	|	0	|	1	|
|-------|-------|-------|
|	1	|	1	|	1	|
|-------|-------|-------|

NOT Table: -
---------
|-------|-------|
|	X	|  ~X   |
|-------|-------|
|	0	|	1	|
|-------|-------|
|	1	|	0	|
|-------|-------|

Note: To find more than one digit, first add 1 to that digit then inverse the MSB (Most Significant Bit).

XOR Table: -
---------
|-------|-------|-------|
|	X	|	Y	| X ^ Y |
|-------|-------|-------|
|	0	|	0	|	0	|
|-------|-------|-------|
|	0	|	1	|	1	|
|-------|-------|-------|
|	1	|	0	|	1	|
|-------|-------|-------|
|	1	|	1	|	0	|
|-------|-------|-------|

RIGHT-SHIT Table (DEL any bit from LSB): -
---------------------------------------
|-------|-------|---------|
|	X	|	Y	| X >> Y  |
|-------|-------|---------|
				| X / 2^Y |
				|---------|

LEFT-SHIFT Table (ADD 0 bit from LSB): -
-------------------------------------
|-------|-------|---------|
|	X	|	Y	| X << Y  |
|-------|-------|---------|
                | X * 2^Y |
                |---------|

1's Complement: inverse of every bits.
2's Complement: adding 1 to 1's complement.

'''

def dec_to_bin(dec: int) -> str:
	bin = ''
	# <- resume

def count_bits(num: int) -> int:
	count = 0
	while num:
		count += 1
		num >>= 1
	return count

def fun1(x: list) -> int:
	'''
		Use of XOR operator - If all value occur twice except one value, then it can find that one value.
		Time : O(n), because it will iterate through all values.
		Space: O(1), because it doesn't contain any value.
	'''
	unique_value = 0
	for i in x:
		unique_value ^= i
	return unique_value

#print(fun1([1,2,3,4,1,2,4]))

def fun2a(num: int) -> str:
	'''
		Find whether a number is EVEN or ODD using % (Modulo Operator)
		Note: -
			% (Modulo Operator) is faster than & (AND Operator)
	'''
	if (num % 2) != 1:
		return "EVEN"
	else:
		return "ODD"

def fun2b(num: int) -> str:
	'''
		Find whether a number is EVEN or ODD using & (AND Operator)
		Note: -
			& (AND Operator) is slower than % (Modulo Operator)
	'''
	if (num & 1) != 1:
		return "EVEN"	# LSB (Least Significant Bit) is 0
	else:
		return "ODD"	# LSB (Least Significant Bit) is 1

#n = int(input('Ener a number: '))
#print(f'% -> {fun2a(n)}')
#print(f'& -> {fun2b(n)}')

def fun3(num: int) -> None:
	'''
		Find whether given position bit is 0 / 1.
	'''
	if num == 0:
		print(f'BIT POSITION 1: 0')
	max_bits = count_bits(num)
	for i in range(max_bits):
		mask = 1 << i
		if (num & mask) > 0:
			print(f'BIT POSITION {max_bits - i}: 1')
		else:
			print(f'BIT POSIITON {max_bits - i}: 0')

#n = int(input('Enter a number: '))
#fun3(n)
