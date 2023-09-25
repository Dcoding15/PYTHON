#! /usr/bin/python3

#	List Comprehension: -

# Taking multiple input in single line in list
'''
a = [ eval(x) for x in input('Enter number: ').split() ]
print(a)
# Output: [10, 20, 30, 40, 50, 60]
'''

# l = [ expression for variable in sequence ]
# Printing multiple of 2 from 1 to 10
'''
l = [ i*2 for i in range(1, 11) ]
print(l)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''

#l = [ expression for variable in sequence if condition ]
# Printing even number from 1 to 10
'''
l = [ i for i in range(1, 11) if i%2 == 0 ]
print(l)
# Output: [2, 4, 6, 8, 10]
'''

#	Set Comprehension: -

# Taking multiple input in single line in set
'''
a = { eval(x) for x in input('Enter number: ').split() }
print(a)
# Output: {40, 10, 50, 20, 30}
'''

# s = { expression for variale in sequence }
# Printing multiple of 2 from 1 to 10
'''
s = { i*2 for i in range(1, 11) }
print(s)
# Output: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
'''

# s = { expression for variable in sequence if condition }
# Printing even number from 1 to 10
'''
s = { i for i in range(1, 11) if i%2 == 0 }
print(s)
# Output: {2, 4, 6, 8, 10}
'''

# Dictionary Comprehension: -
'''
x = 65
d = { chr(x+i):i*100 for i in range(26) }
print(d)
# Output: {'A': 0, 'B': 100, 'C': 200, 'D': 300, 'E': 400, 'F': 500, 'G': 600, 'H': 700, 'I': 800, 'J': 900, 'K': 1000, 'L': 1100, 'M': 1200, 'N': 1300, 'O': 1400, 'P': 1500, 'Q': 1600, 'R': 1700, 'S': 1800, 'T': 1900, 'U': 2000, 'V': 2100, 'W': 2200, 'X': 2300, 'Y': 2400, 'Z': 2500}
'''

# Merging of Collections: -
