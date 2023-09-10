#! /usr/bin/python3

'''
Exception Handling: -
	1. Error is an unexpected event which disturbs the normal flow of program. To handle such error we use exception handling.
	2. Exception handling is a way to handling error by generating modified output to continue rest of program normally.
	3. Every exceptions are child classes of BaseException (root of python's exception hirarcy)
	4. If an exception raised within try block, then rest of the code within try block won't get executed.
	5. If any exception raised outside try block, then the error will disrupt the normal flow of program.
	6. Except block will always catch error even if we don't provide any exeptions name. It is also called default except block. It must be at last position among except blocks.
	7. The statement within finally block will considered most prioritise statement.

	Syntax:-
	------
	try:														# try block will execute as normal flow of program
		#statement-1
		#statement-2
		#statement-3
		#statement-4
	except (Exception1, Exception2, ..., ExceptionN) as msg:	# except block will catch error
		print(msg)												# print modified error message
	else:														# else will execute if except block doesn't catch any error
		#statement-5
		#statement-6
	finally:													# Finally block will always going to execute
		#statement-7

Nested try-except-finally block: -
-------------------------------
try:						#outer try block
	#statement-1
	try:					#inner try block
		#statement-2
	except error_name1:		#except inner block
		#statement-3
	finally:				#finally inner block
		#statement-4
	#statement-5			#inside statement
except error_name2:			# except outer block
	#statement-6
finally:					#finally outer block
	#statement-7
#statement-8				#outside statement

	1. No exception then outer try block ----> inner try block ---> inner finally block ---> inside statement ---> outside statement will execute.
	2. Exception at statement-1 and outer except block matched then outer except block ---> outer finally block ---> outside statement will execute.
	3. Exception at statement-1 and outer except block not matched then outer finally block will execute.
	4. Exception at statement-2 and inner except block matched then outer try block ---> inner except block ---> inner finally block ---> inside statement ---> outer finally block ---> outside statement will execute.
	5. Exception at statement-2 and inner except block not matched but outer except block matched then outer try block ---> inner finally block ---> outer except block ---> outer finally block ---> outside statement will execute.
	6. Exception at statement-2 and inner and outer except block both are not matched then outer try block ---> inner finally block ---> outer finally block will execute.
	7. Exception at statement-3 and outer except block matched then outer try block ---> inner finally block ---> outer except block ---> outer finally block ---> outside statement will execute.
	8. Exception at statement-3 and outer except block not matched then outer try block ---> inner finally block ---> outer finally block will execute.
	9. Exception at statement-4 and outer except block matched then outer try block ---> inner try block ---> outer except block ---> outer finally block ---> outside statement will execute.
	10. Exception at statement-4 and outer except block not matched then outer try block ---> inner try block ---> outer finally block will execute.
	11. Exception at statement-5 and outer except block matched then outer try block ---> inner try block ---> inner finally block ---> outer except block ---> outer finally block ---> outside statement will execute.
	12. Exception at statement-5 and outer except block not matched then outer try block ---> inner try block ---> inner finally block ---> outer finally block will execute.
	13. Exception at statement-6 outer try block ---> inner try block ---> inner finally block ---> outer finally block will execute and also disrupt flow of program.
	14. Exception at statement-7 and statement-8 then outer try block ---> inner try block ---> inner finally block ---> outer except block will execute will be executed and also disrupt the flow of program.
'''
