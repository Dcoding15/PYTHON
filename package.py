#! /usr/bin/python3

'''

From python3.3 version onwards __init__.py file is optional.
In python package __init__.py will execute first before every execution of main program.

		Python package: -
			1) Collection of modules ( collection of function and variables ) / file.
			2) It is simply a folder or directory.
			3) It is an encaplsulation module to group related modules into single unit.
			4) It also contain sub-packages.
			5) It must contain __init__.py file. If we are using IDE then it will automatically create __init__.py file otherwise we have to create file manually.
			6) It is optional to create __init__.py file.

		Advantages: -
			1. We can resolve naming conflicts.
			2. We can idntify our components uniquely.
			3. It improves grouping of compoenent.
			4. It improves readability and maintainablity.

		Importance of __init__.py file: -
		------------------------------
			1. To perform initialization activities, so that we can execute automatically.

		Need of installing a package: -
		----------------------------
		If we want to use a package, compulsory it should be available in the current working directory. To make package available throughout the system then we have to install that package.


		How to install a package throughout the system: -
		----------------------------------------------
		1. We have to make setup.py file and import setup() function from setuptools modules.
		2. In setup.py file we have give arguments to setup() function i.e., setup(name='name_of_library_to_install', version='version_number', packages=['name_of_packages'])
		3. To install python packages all over the system, we have to use pip (pip install packages) command. Pip is a python package management system to install and manage software packages written python.
		Command to install: pip install [ directory_name / package_name ]
		Command to uninstall: pip uninstall [ directory_name / package_name ]
		4. Alternative way,
			from setuptools import setup, find_packages()
			setup(
				name='name_of_library_to_install',
				version='version_number',
				packages=find_packages()
			)

		Note 1: packages=['name_of_packags'] <-- this will only install the named packages.
			  packages=find_packages()     <-- this function will install all the packages present within a directory.
			  We have to give __init__.py file to every package (FOR SAFETY PURPOSE).

		Note 2: pip install django   <-- This is for web framework
				pip install pymysql	 <-- This is for mysql client
				pip instal selenium  <-- This is for automation
				pip install faker	 <-- This is for generating fake data

'''
