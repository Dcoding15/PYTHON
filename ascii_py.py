#! /usr/bin/python3

# From 0 to 32 and 127 are non-printable characters
# From 33 to 126 are pritable characters

def ascii():
	for i in range(33, 127):
		print(i,'=',chr(i))

ascii()
