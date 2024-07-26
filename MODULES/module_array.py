#! /usr/bin/python3

'''
array(typecode, [iterable_value]) -> array

Type code   C Type             Minimum size in bytes

'b'         signed integer     1
'B'         unsigned integer   1

'h','i'     signed integer     2
'H','I'     unsigned integer   2

'l'         signed integer     4
'L'         unsigned integer   4

'q'         signed integer     8
'Q'         unsigned integer   8

'u'         Unicode character  2

'f'         floating point     4
'd'         floating point     8


Methods:

buffer_info()     --> return (address, length)
byteswap()        --> byteswap all the items of the array
count(v)          --> return number of occurrences of v in an object
index(v)          --> return index of first occurrence of v in an object

append(v)         --> append a new_value to the end of the array
insert(n, v)      --> insert a v into the array at n position
extend([])        --> extend array by appending multiple elements from an iterable

pop()             --> remove and return item
remove(v)         --> remove first occurrence of v in an object

reverse()         --> reverse the order of the items in the array

fromlist(l)       --> append items from the list l
tolist()          --> return the array converted to an ordinary list

frombytes(buff)   --> append items from the string buffer buff
tobytes()         --> return the array converted to a string buffer

fromfile(f, n)    --> append n items from a file object f
tofile(f)         --> return all items to a file object f

fromunicode(ustr) --> append items from the unicode string ustr
tounicode()       --> return the array converted to an unicode string

Attributes:

typecode      -- return type of array
itemsize      -- the length in bytes of one array item

'''
