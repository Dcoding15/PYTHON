#! /usr/bin/python3

'''

Generator: -
---------
	1. It is a function which doesn't return any value. It acts as iterator.
	2. Generate a sequence of values i.e., it will generate one value and returns then remove value.
	3. Use special keyword called yield to generate objects (sequence of values). yield is only used for generators which acts as return.
	4. Not create objects from beginning like traditional collections.
	5. Not terminate from program.
	6. Stop iteration if we print more than the number of times than no. of values present inside yield.
	7. Faster than traditional collections.
	8. Memory wise recommended.
	9. Can handle huge no. of data.
	10. Data won't stored. Therefore, we can't access particular document.
	11. By using list() we can convert generator into list.

	Example:-
	#Fibonacci Sequence with generator
	def fibog(n):
        a,b = 0,1
        while n:
            c = a + b
            yield a			#will return value on at a time
            a = b
            b = c
            n -= 1

x = int(input())

for i in fibog(x):
        print(i)
'''