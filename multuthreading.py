#! /usr/bin/python3

'''
Multi-threading: -
---------------
	1. Multithreading is a programming concept that allows a program to create small tasks that can be executed in parallel. This allows a program to use a CPU more efficiently.
	2. Executing several task simultaneously is called multi-tasking. There are two types: -
		(a) Process based multi-tasking: Each task is a seperate independent process. It is suitable of operating system level.
		(b) Thread based multi-tasking: Each task is a seperate independent part of the same program. It is suitable for programmatic level.
	3. Thread is flow of execution. It is an independent part of same program.
	4. Multithreading is possible by using threading, time, queue module.
	5. Process running using threading module are called child thread and those process running without using threading module are called main thread. The main thread will always execute first.
	6. Creation of thread: -
		(a) Create thread without using thread class. (By simply using thread object)
		(b) Create thread with by extending thread class. (By extending Thread class and overriding run() method)
		(c) Create thread without extending thread class. (By creating normal class, then creating its object and using thread object)
	7. There is identification number to each running thread and we can't change or set our own identification number because it is set by PVM (Python Virtual Machine).
	8. Threads which are running in backgroud is called daemon threads. Main thread is always non-daemon threads. By default, daemon nature of child thread are same of their parent thread.
'''