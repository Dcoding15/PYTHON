#! /usr/bin/python3

'''

Modules: -
-------
	A group of functions, variables and classes saved to a file. Every python file is module. If we create a module then automatically python compiled file (.pyc file) will be created (which is inside __pycache__ directory). It is created to improve performance.

    If we are importing module from different location, then at the time of importing we have to specify location along with module

Advantages: -
----------
	(1) Code Re-usability
    (2) Readability
    (3) Maintainability
    (4) Reduce development time
    (4) Reduce cost of the project

Types of ways to import modules: -
import py_file_name
from py_file_name import * (In place of * we can specify members of that py_file_name)
from py_file_name import member_name1 as variable_name1, member_name2 as variable_name2, ...
import py_file_name as variable_name


Module Naming conflicts: -
-----------------------
	(1) Python will consider most recent copy.
    (2) 2 ways to avoid naming conflicts: -
		(A) import py_file_name
        (B) from py_file_name import member_name1 as variable_name1, member_name2 as variable_name2, ...

Reloading of module: -
-------------------
	(1) By default module will load once even after importing multiple times.
	(2) To reload module we have to use reload() from imp module. It is a depriciated module.

Finding members of modules using dir(): -
--------------------------------------
	1st way: dir() will list out the members of current module.
    2nd way: dir(module_name) will list out the members of specified module.
Note: -
----
	(1) We can define doc string using ''' ''' or """ """. We can display doc string using __doc__
	(2) We can display the current file name using __file__
	(3) __name__ ==> __main__ is executing specified module as main program. This is direct execution.
				 ==> module_name. This is indirect execution.
	(4) if __name__:'__main__':
				# code
		The above will acts as a main function in python3

'''
