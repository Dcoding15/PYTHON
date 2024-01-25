#! /usr/bin/python3
'''
File Handling: -
-------------

If sepecified file is not mentioned then with the 'w' (write) and 'a' (append) mode, it genreate that file automatically.
We can also use 'x' (exclusive creation) mode to create a file. If the specified file exit then it return FileExitsError.
By default the file will operate in text mode i.e., 't' and we can switch to binary mode using 'b'
We can use only one operation between read, write append. It we use all operation together then it return ValueError

Files are common permanent storage areas to store our data. It is recommend to store small amount of data. For storing big amount of data we have to use databases.

Temporary storage areas: Data is available as long as programming is running. After the execution of program data will be gone. Example of temporary storage areas simple variables, list, set, etc.

Permanent storage areas: These are the storage areas where data stored for long period of time i.e., after the execution of program data will be stored. Example of permanent storage areas are files, databases, big data technologies.

Why file for short data not for big data ?
ans) 1. limited file size
	 2. operationg will become difficult
	 3. less security

There are 2 types of files: -
	1. text files like .txt, .py, etc
	2. binary files like image files, audio files, etc

Various properties of file object: -
---------------------------------

	f = open('file_name', 'mode')	<-- opening file with its given mode
	
	f.closed()						<-- return True if file is closed, otherwise False.
	f.detach()						<--
	f.fileno()						<--
	f.flush()						<--
	f.isatty()						<--
	f.tell()						<--	return position of cursor (file pointer) of file.
	f.mode()						<-- return which mode is selected.
	f.name()						<-- return name of file.

	f.seek(N)						<-- move cursor (file pointer) to the Nth position of file.
	f.seekable()					<-- return whether file allow to change cursor (file pointer).

	f.turncate()					<--

	f.readable()					<-- return True if file is readable file, otherwise False.
	f.read(N)						<-- return N no. of character from the file. If we don't provide N as input then it will return all character from file.
	f.readline()					<-- return only one line from the file.
	f.readlines()					<-- return list of one line from file.

	f.writeable()					<-- return True if file is writeable file, otherwise False.
	f.write()						<-- It take only a string data-type as an argument and write only in single line without any new line.
	f.writelines()					<-- It can take any type of data-type argument like list, tuple, set, dictionary, string and write only in single line without any new line.

Note: -
----
	1. After using read methods the cursor will move to next position of the Nth character.
	2. why close() method is used in file.
	   ans: Because the system resources may got blocked. So, it is highly recommeded to close the file pointers using close() method.

Modes for open() function: -
-------------------------

Note: These are used only for text file.
There are 7 modes in open() function i.e., r, w, a, r+, w+, a+, x

For binary file: rb, wb, ab, r+b, w+b, a+b, xb.

For 'r' ==> read operation: -
	(1) Open an existing file for read operation
	(2) The file pointer is at the begenning of the file.
	(3) If the specified file is not available the FileNotFoundError.
	(4) The default mode is read mode.

For 'w' ==> write operation: -
	(1) Open an existing file for write operation.
	(2) The existing file should overwrite all data.
	(3) If the specified file is not available then it will create that file and write the input data.

For 'a' ==> append operation: -
	(1) Open existing file for append operation.
	(2) It doesn't overwrite the existing data.
	(3) If the specified file is not available then it will create that file and write the input data.

For 'r+' ==> To read and write operation: -
	(1) It won't overwrite the existing data. Because this operation will first read and then write data.
	(2) If the specified is not available then it will give FileNotFoundError.

For 'w+' ==> To write and read operation: -
	(1) It overwrite the existing data. Because this operation will first write and then read data.
	(2) It will create new file if the specified file is not there.

For 'a+' ==> To append and read operation: -
	(1) It doesn't ovewrite the existing data it only appends data and then perform read operation.
	(2) It will create new file if the specified the file is not there.

For 'x' ==> exclusive creation mode: -
	(1) It is used to perform write operation. If the spcified file is not there then it will give FileExistsError.

with statement: -
--------------
	1. File will be closed automatically.
	2. Group file related operation within a block to improve readability.

'''

# Exclusive creation file
# with open('demo.txt', 'x') as f:
# 	f.close()

# Write operation
# This built-in function is used to open any to perform file operation
'''
with open('demo.txt', 'w') as f:		# This is equivalent to f = open('demo.txt')
	if( f.writable() == True ):			# To check weather file is writeable or not
		f.write('Write operation supported\n')
	else:
		print('Write operation is not supported')
	f.close()	# This built-in function is used to close opened file
'''

# Append operation
'''
with open('demo.txt', 'a') as f:
	if( f.writable() == True ):			# To check weather file is writeable or not
		f.write('Append operation supported\n')
	else:
		print('Append operation is not supported')
	f.close()
'''

# Read operation
'''
with open('demo.txt', 'r') as f:
	if f.readable() == True:			# To check weather file is readable or not
		print(f.read())
		print('Read operation supported')
	else:
		print('Read operation is not supported')
	f.close()
'''
