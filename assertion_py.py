#! /usr/bin/python3
'''
Assertion: -
---------
	1. The main purpose of assertion is for debugging purpose.
	2. The process of identifying and fixing the bug is called debugging. The unexpected output from any line of source code is called bug.
	3. Deviation between original and expected output in an testing environment is called defect.
	4. Bydefault assertions is enabled in python. We can disable at time of execution i.e., python -O file_name.py
	5. There are two types of assertion: -
		(a) Simple version: -
			--------------
			Syntax: assert conditional_expression
			1. If conditional_expression returns True then there is no problem upto that and continue its execution.
			2. If conditional_expression returns False then there is problem upto that and stop its execution and raise AssertionError.

		(b) Argumented version: -
			------------------
			Syntax: assert conditional_expression,user_message
	6. Difference between assertion and exceptional handling is that exceptional handling is used to handle runtime errors and assertion is to handle errors at the of development time.
'''