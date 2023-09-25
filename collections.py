#! /usr/bin/python3

# Collections in Python 3
# Collection are heterogenous.
# Collection having dynamic size of input.

def f(lst):
# lst is a iteratable variable
	for i in lst:
		print(i, end=" ")
	print()

# LISTS

# Lists are mutable i.e., we can modify the lists.
# Type cast function is list()
# Lists support + (concatenation) and * (repeatation).
# Lists are non-hasable and we can't use in dictionary.

veg = ['tomato', 'potato', 'onion', 'capcicum']
pet = ['dog', 'cat', 'mouse', 'snake', 'rabbit', 'parrot']

#veg.extend(pet)				# This function will add another list from behind.
#veg2 = veg.copy()			# This function will make shallow copy of original one.
#veg.append('bhopal')		# This function will add at the end of the list.
#veg.remove(veg[3])			# This function will remove the specified element of the list.
#veg.pop()					# This function will remove the element at end of the list.
#veg.insert(2, 'goa')		# This function will add the element at the specified index of the list.
#veg.sort()					# This function wil sort the sequence of the list of similar data types in ascending order.
#veg.reverse()				# This function will return the list in reverse order (not the reverse sequence).
#veg.clear()				# This function will remove all the elements from the list.
#del veg[:3]				# This del keyword is use to remove single element and group of element of the list.
#print( veg.count(veg[3]) )	# This count function will count how many times a specific element occured.
#print( veg.index(9) )		# This index function will return index of element in list.

# TUPLES

# Tuples are immutable i.e., we can't modify the tuples.
# Type cast function is tuple()
# Empty tuple t=()
# Defining a tuple must contain one element and comma ','. For example: t=(234) is not a tuple. But t=(234,) is a tuple.
# In tuples () are optional. For example: t=10,20,30,40 and t=23, is a tuple.
# Tuples takes less memory than list to store some data.
# Tuples support + (concatenation) and * (repeatation).
# Tuples are hashable and we can use in dictionary.

fruit = ('apple', 'banana', 'guava', 'orange', 'grapes', 'apple', 'apple')

#print( fruit.index('orange') )		# This index function will return index of element in list.
#print( fruit.count('apple') )		# This count function will count how many times a specific element occured.

# SETS

# Sets is a collection with unordered and with no duplicate values.
# Type cast function is set() and frozenset() <-- For frozen set (It is immutable and has property of sets).
# It doesn't support indexing and slicing.
# The set({}) will treat as empty dictionary i.e., dict({}) or type will be dictionary.
# Set doesn't support + (concatenation) and * (repeatation).
# Empty set can be created using set()
# It is hashable.
	#s.add([10,20,30]) # this will not add because list is unhashable
	#s.add((10,20,30)) # this will add to set object but it consider all elements as one object
	#s.update(range(1,10)) # here numbers are add from 1-9
	#s.update([10,20,30]) # this will add number to set object
'''
Mathematical operation on the set date structure:
-------------------------------------------------

1. union ==> addition of two or more sets. Symbol for union is |
2. intersection ==> common element between two or more sets. Symbol for intersection is &
3. difference ==> let assume A and B are two sets, A-B means removing elements of B from A and B union and vice versa. Symbol for difference is -
4. symmetric difference ==> contains all element except their common elements. Symbol for symmetric difference is ^
'''

a={1,2,3,4,5}
b={4,5,6,7,8}
city = {'Kolkata', 'Bhopal', 'Chennai', 'Bangalore', 'Delhi'}
city2={'Kolkata', 'Chennai', 'Delhi', 'Mumbai'}

s = set()	# It is an empty set
#city.add('Patna')												  # This function will add the element in the set.
#s.add([10,20,30]) # this will not add because list is unhashable
#s.add((10,20,30)) # this will add to set object but it consider all elements as one object
#city.remove('Kolkata')											  # This function will remove the element from the set.
#city.clear()													  # This function will remove all the element from the set.
#city.update(veg)												  # This function will add all the elements from any iteratable variables.
#s.update(range(1,10)) # here numbers are add from 1-9
#s.update([10,20,30]) # this will add number to set object
#city2 = city.copy()											  # This function will make shallow copy of original one.
print('UNION: ',city.union(city2))								  # This function will return union set and and other iterable variable.
print('INTERSECTION: ',city.intersection(city2))				  # This function will return intersection between set and other iterable variable.
print('DIFFERENCE: ',city.difference(city2))					  # This function will return difference between set and other  iterable variable.
print('SYMMETRIC DIFFERENCE: ',city.symmetric_difference(city2)) # This function will return symmetric difference between set and other iterable variable.
print("A=",a)
print("B=",b)
print("Union is",(a|b))
print("Intersection is",(a&b))
print("Difference is",(a-b))
print("Symmetric difference is",(a^b))

# Note: union, intersection, difference is only used by set on other iteratable variables ( including set variables).

# DICTIONARIES

# Dictionaries is a changeable, unordered collection of unique key:value pairs. It is fast because it use hashing, allow us to access a value quickly.
# Key and value pair can be different data types.
# Keys can't be duplicate
# It doesn't support indexing and slicing.
# Type cast function is dict()
# Empty dictionary can be created using {}
'''
d = dict({'fname':'Debrishi','lname':'Biswas','age':19,'city':'Kolkata'})			#Normal dictionary declaration
e = dict([('fname','Debrishi'),('lname','Biswas'),('age',19),('city','Kolkata')])	#List of value,pair in tuples
f = dict([['fname','Debrishi'],['lname','Biswas'],['age',19],['city','Kolkata']])	#List of value,pair in lists
g = dict({('fname','Debrishi'),('lname','Biswas'),('age',19),('city','Kolkata')})	#Set of value,pair in tuple
'''

info = {'first_name':'Debrishi', 'last_name':'Biswas', 'age':19, 'state':'Kolkata'}
info1 = {'course':'BCA', 'university':'Brainware University'}

#print(info['first_name'])									# It will return the value of key in dictionary.
#print(info.get('first_name'))								# It will same as info['first_name']. We can also specify default value (dict().get(key, default_value))
#print(info.keys())											# This function will only return all keys in dictionary. Similarly, print(list(info)) are same.
#print(info.values())										# This function will only return all values in dictionary.
#info.update(info1)											# This function will add all the elements from dictionary variables.
#print(info.items())										# This function will return the entire key:value pair in dictionary.
#info.clear()												# This function will remove all the elements from the dictionary
#info2 = info.copy()										# This function will make a shallow copy of original one.
#del info['age']											# This function will remove the specified key:value from dictionary. Similarly, info.pop('age') are same.
#info.popitem()												# This function will remove the elements from dictionary using LIFO.
#info.pop('age')											# This function will remove the specified element from dictionary.
#info.setdefault('age', 18)									# This function will only set default value of corresponding key.
#print(info.fromkeys({'student code'}, 'BWU_BCA_21_195'))	# This function will return copy of dictionary, where argument of 1st parameter shouldn't be string


'''

# We can print like below mentioned: -

for i, j in info.items():
	print(i,':',j)

'''

# Note: Dictionary doesn't compared if they don't have same keys.

# Merging collection

'''
l = [i for i in range(1,4)]
t = 4,5,6
s = {i for i in range(6,9)}
d1 = {chr(65+i):(i+1)*100 for i in range(5)}
d2 = {chr(65+i):(i+1)*100 for i in range(5,10)}
r = *l,*t,*s,*d1.keys(),*d1.values(),*d2.keys(),*d2.values()
r1 = *d1.items(),*d2.items()
print('l =',l)
print('t =',t)
print('s =',s)
print('d1 =',d1)
print('d2 =',d2)
print('list of r =',list(r))
print('tuple of r =',tuple(r))
print('set of r =',set(r))
print('dictionary of r1 =',r1)
'''

# Output: -
#l = [1, 2, 3]
#t = (4, 5, 6)
#s = {8, 6, 7}
#d1 = {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}
#d2 = {'F': 600, 'G': 700, 'H': 800, 'I': 900, 'J': 1000}
#list of r = [1, 2, 3, 4, 5, 6, 8, 6, 7, 'A', 'B', 'C', 'D', 'E', 100, 200, 300, 400, 500, 'F', 'G', 'H', 'I', 'J', 600, 700, 800, 900, 1000]
#tuple of r = (1, 2, 3, 4, 5, 6, 8, 6, 7, 'A', 'B', 'C', 'D', 'E', 100, 200, 300, 400, 500, 'F', 'G', 'H', 'I', 'J', 600, 700, 800, 900, 1000)
#set of r = {1, 2, 3, 4, 5, 6, 7, 8, 900, 400, 'D', 'J', 800, 'H', 'F', 300, 'B', 700, 'I', 'G', 'C', 200, 600, 'E', 'A', 100, 1000, 500}
#dictionary of r1 = (('A', 100), ('B', 200), ('C', 300), ('D', 400), ('E', 500), ('F', 600), ('G', 700), ('H', 800), ('I', 900), ('J', 1000)

# Nested collection

'''
l = [(1,2,3),{4,5,6},{'A':10,'B':20,'C':30}]
t = ([1,2,3],{4,5,6},{'A':10,'B':20,'C':30})
s = {(4,5,6)}		# We can't give list and dictionary as it is unhashable to set
d = {(4,5,6):'F'}	# We can't give list and set as key because it is unhashable to dictionary
print(l)			#[(1, 2, 3), {4, 5, 6}, {'A': 10, 'B': 20, 'C': 30}]
print(t)			#([1, 2, 3], {4, 5, 6}, {'A': 10, 'B': 20, 'C': 30})
print(s)			#{(4, 5, 6)}
print(d)			#{(4, 5, 6): 'F'}
'''
