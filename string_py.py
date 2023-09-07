#! /usr/bin/python3

# STRINGS


# Escape Sequence					Meaning
#	\							Newline Ignored
#
#	\\							Backslash ( \ )
#	\'							Single quote ( ' )
#	\"							Double quote ( " )
#	\a							ASCII BEL
#	\b							ASCII Backspace
#	\f							ASCII Formfeed
#	\n							ASCII Linefeed
#	\r							ASCII Cariage Return
#	\t							ASCII Horizontal Tab
#	\v							ASCII Vertical Tab
#
#	\o---						Character with octal value ---
#	\x---						Character with hexadecimal value ---
#
#	\N{---}						Character named --- in the unicode database
#	\u---						Character with 16-bit hexadecimal value ---
#	\U---						Character with 32-bit hexadecimal value ---

def fun(s):
# This function will return all characters index both positive and negative side
	i = 0
	for j in s:
		print('Character: {} | Positive Index: {} | Negative Index: {}'.format(j, i, i-len(s)))
		i += 1

# Syntax: str().capitalize()
# It return copy of the string with its first character uppercase and rest of the string as a lower case.
#print('debrishi biswas'.capitalize())
# Output: Debrishi biswas

# Syntax: str().title()
# It return copy of the string with first character between whitespace character as uppercase only.
#print('hello, world!'.title())
# Output: Hello, World!

# Syntax: str().lower()
# It return copy of the string with all of its character in lowercase.
#print('ABCDEF'.lower())
# Output: abcdef

# Syntax: str().upper()
# It return copy of the string with all of its character in uppercase.
#print('abcdef'.upper())
# Output: ABCDEF

# Syntax: str().swapcase()
# It return a copy of the string after changing the uppercase to lowercase and vice-versa.
#print('Hello, World!'.swapcase())
# Output: hELLO, wORLD!

# Syntax: str().casefold()
# Example: If any one character has small german letter 'ß' then it should convert it into 'ss'.
# It return a casefolding copy of a string which may be used for caseless matching.

# Syntax: str().expandtabs()
# It return a copy of the string where all tab characters are replaced by 8 spaces (default tabsize).
#print('debrishi\tbiswas'.expandtabs())
# Output: debrishi        biswas

# Syntax: str().zfill(with_of_zeros)
# Return a copy of the string left filled with ASCII '0' to make a string of length width_of_zeros.
# Note: If the width_of_zeros is less than or equal to len(str()), then it return original string.
#print('hello'.zfill(10))
# Output: 00000hello

# Syntax: str().center(width_of_line, which_ascii_character)
# Note: If width is less than or equal to len(str()) then original string will returned.
#print('debrishi biswas'.center(len('debrishi biswas'))+56, '*')
# Output: ****************************debrishi biswas****************************

# Syntax: str().ljust(width_of_line, which_ascii_character)
# It return left justified string with length of width_of_line and which_ascii_character as some character filled.
# Note: If the width is less than or equal to len(str()) then original string will returned.
#print('debrishi'.ljust(len(str('debrishi'))+56, '*'))
# Output: debrishi********************************************************

# Syntax: str().rjust(width_of_line, which_ascii_character)
# It return right justified string with length of width_of_line and which_ascii_character as some character filled.
# Note: If the width is less than or equal to len(str()) then original string will returned.
#print('debrishi'.rjust(len(str('debrishi'))+56, '*'))
# Output: ********************************************************debrishi

# Syntax: str().strip(str())
# It return a copy of a string after removing some specified characters from both left and right side but not between string.
# If the value of the argument is None then it removes only whitespaces characters.
#print('#!!#!#!#!#!#!#!debrishi biswas%!%!%!!%'.strip('!#$%'))
# Output: debrishi biswas

# Syntax: str().lstrip(str())
# It return a copy of a string after removing some specified characters from left side of the string without skipping characters.
# If the value of the argument is None then it removes only whitespace characters.
#print('debrishi123'.lstrip('edrz'))
# Output: brishi123

# Syntax: str().rstrip(str())
# It return a copy of a string after removing some specified characters from right side of the string without skipping characters.
# If the value of the argument is None then it removes only whitespace characters.
#print('debrishi123'.rstrip('ws23'))
# Output: debrishi1

# Syntax: str().count(sub_string, starting_index, ending_index)
# It return number of non-overlapping occurance of substring.
# Note: starting_index and ending_index are optional.
#print('debrishi biswas'.count('i'))
# Output: 3

# Syntax: str().encoding(encoding = 'utf-8', error = 'strict')
# It return encoded version of the string as a byte object.
# Note: By default encoding is 'utf-8' and error is 'strict'

# Syntax: str().endswith(sub_string, starting_index, ending_index)
# It return True if str() ends with sub_string or else it will return False.
# Note: starting_index and ending_index are optional.
#print('debrishi biswas'.endswith('was'))
# Output: True

# Syntax: str().startswith(sub_string, starting_index, ending_index)
# It return True if str() begins with sub_string or else it will return False.
# Note: starting_index and ending_index are optional.
#print('debrishi biswas'.startswith('deb'))
# Output: True

# Syntax: str().find(sub_string, starting_index, ending_index)
# It return lowest index in the string where sub_string is found or else return -1 if not found.
# Note: starting_index and ending_index are optional.
#print('debrishi'.find('i'))
# Output: 4

# Syntax: str().rfind(sub_string, starting_index, ending_index)
# It return highest index in the string where sub_string is found or else return -1 if not found.
# Note: starting_index and ending_index are optional.
#print('debrishi'.rfind('i'))
# Output: 7

# Syntax: str().index(sub_string, starting_index, ending_index)
# It is same as str().find(sub_string, starting_index, ending_index), but if the sub_string is not found then it raises ValueError.

# Syntax: str().rindex(sub_string, starting_index, ending_index)
# It is same as str().rfind(sub_string, starting_index, ending_index), but if the sub_string is not found then it raises ValueError.

# Syntax: str().format(arg1, arg2, arg3, ...)
# It return a copy of a string after replacing {}
#print('My name is {fname} {lname} and I\'am {age} yrs old'.format(fname = 'Debrishi', lname = 'Biswas', age = 19))
# Output: My name is Debrishi Biswas and I'am 19 yrs old
#print('My name is {0} {1} and I\'am {2} yrs old'.format('Debrishi','Biswas',19))
# Output: My name is Debrishi Biswas and I'am 19 yrs old
#print('My name is {} {} and I\'am {} yrs old'.format('Debrishi','Biswas',19))
# Output: My name is Debrishi Biswas and I'am 19 yrs old

# str().replace(old_string, new_string, count)
# It return a copy of a string after replacing old_string with new_string at first occurrence.
# Note: count (number of occurrence restrict upto) is int() and it is optional, if we not give then all old_string will replace.
#print('i am a good programmer and good boy'.replace('good', 'legend', 1))
# Output: i am a legend programmer and good boy

# Syntax: str().isalpha()
# It return True if all the characters are only alphabetic, otherwise return False.
#print('abcd'.isalpha())
# Output: True

# Syntax: str().isalnum()
# It return True if all the characters are only alphabetic and numeric, otherwise return False.
#print('asv123'.isalnum())
# Output: True

# Syntax: str().isascii()
# It return True if all the characters are all ascii characters, otherwise return False.
#print('!@#123ABCabc'.isascii())
# Output: True

# Syntax: str().isdecimal(), str().isdigit()
# It return True if all the characters are numeric characters (base 10), otherwise return False.
#print('1223'.isdecimal())
# Output: True
#print('1223'.isdigit())
# Output: True

# Syntax: str().isidentifier()
# It return True if string is a valid identifier according the language definition, otherwise return False.
#import keyword
#print('for'.isidentifier(), keyword.iskeyword('for'))
# Output: True True
#print('num1'.isidentifier(), keyword.iskeyword('num1'))
# Output: True False

# Syntax: str().islower()
# It return True if string is in lowercase, otherwise return False.
#print('my name is debrishi biswas'.islower())
# Output: True

# Syntax: str().isupper()
# It return True if string is in uppercase, otherwise return False.
#print('DEBRISHI'.isupper())
# Output: True

# Syntax: str().isnumeric()
# It return True if string have only numeric characters, otherwise return False.
#print('123234'.isnumeric())
# Output: True

# Syntax: str(),isprintable()
# It return True if the string has printable ascii or it is empty.
#print('\u0001'.isprintable())
# Output: False
#print('hello, world!'.isprintable())
# Output: True

# Syntax: str().isspace()
# It return True if string has only whitespace character, otherwise return False
#print('    '.isspace())
# Output: True
#print('good morning'.isspace())
# Output: False

# Syntax: str().join(iterable_variable)
# It return copy of string after concatenation with every character of iterable_variable with full string.
# The string are first and last character of iterable_variable.
#print('debrishi'.join('1234'))
# Output: 1debrishi2debrishi3debrishi4

# Syntax: str().partition(seperator_string)
# At the first occurrence of seperator_string it splits and return a 3-tuple containing the part before the separator, the separator itself, the part after the separator.
# If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings
#print('mynameishello'.partition('eis'))
# Output: ('mynam', 'eis', 'hello')
#print('mynameishello'.partition('yae'))
# Output: ('mynameishello', '', '')

# Syntax: str().rpartition(seperator_string)
# At the first occurrence of seperator_str it splits and return a 3-tuple containing the part before the separator, the separator itself, the part after the separator.
# If the separator is not found, return a 3-tuple containing two empty string, followed by the string itself.
#print('mynameishello'.rpartition('eis'))
# Output: ('mynam', 'eis', 'hello')
#print('mynameishello'.rpartition('yae'))
# Output: ('', '', 'mynameishello')

# Syntax: str().split(seperator_string, max_occur) / str().rsplit(seperator_string, max_occur)
# After spilting of string on basis on seperator _string, then it return list of split string.
# Note: max_occur is int() and it is use to limit maximum occurance (it is optional).
#print('delhi,mumbai,chennai,kolkata,jaipur'.split(','))
# Output: ['delhi', 'mumbai', 'chennai', 'kolkata', 'jaipur']

# Syntax: str().removeprefix(prefix_string)
# It return a copy of a string after removing the prefix_string (starting from left side of string).
#print('iamprogrammer'.removeprefix('iam'))
# Output: programmer

# Syntax: str().removesuffix(suffix_string)
# It return a copy of a string after removing the suffix_string (starting from right side of string).
#print('iamprogrammer'.removesuffix('programmer'))
# Output: iam

'''
Note: -
	1. By using str(), we can convert the given object into string but reverse is not possible.
	2. By using repr(), we can convert the given object into string and reverse is also possible.
	3. By using __repr__() returns the official string representation, which is aimed at programmers as they develop and maintain a program.
	4. By using __str__() returns the informal string representation, a friendlier format for the program's user.
'''