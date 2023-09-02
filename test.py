#! /usr/bin/python3

'''

pass - It's function is only to execute with no return.
del - It is means to delete any reference object.

for-else loop: -
for i in range(10):
	print(i)
else:
	print('okay')
Output: -
0
1
2
3
4
5
6
7
8
9
okay

while-else loop: -
i = 0
while(i < 10):
	print(i)
	i += 1
else:
	print('okay')
	del i
Output: -
0
1
2
3
4
5
6
7
8
9
okay

'''


'''

Packing and Unpacking in Tuple: -
---------------------------------

Packing: -
----------
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)
#Output: (10, 20, 30, 40)

Unpacking: - In unpacking tuple number of variable and value should be equal.
------------
t=(10,20,30,40)
a,b,c,d=t
print(a,b,c,d)
#Output: 10 20 30 40

Tuple hashing: -
----------------
d={(12,34,22):'hello'}
print(d[12,34,22])
#Output: hello
'''
