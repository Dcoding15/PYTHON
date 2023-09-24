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

	Synchronization: -
	---------------
		1. If threads are executing simultaniously then there may be a chance of race condition (data inconsistency). To overcome race condition we have execute only one thread at a time.
		2. There are three techniques of synchronisation: Lock, R-Lock, Semaphore.
	
		Lock: -
		----
			1. Lock().acquire()	---> one thread will be locked
			2. Lock().release() ---> one thread will be released
			3. It will allow to lock one thread at a time i.e., locking more than one thread will create deadlock.
		
		RLock (Reentrante Lock): -
		-----------------------
			1. It's methods are same as Lock() but the only difference is it will relock another thread after removing previous thread.
			2. It automatically release lock if working of thread is completed.
		
		Semaphore: -
		---------
			1. A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call.
			2. The counter can never go below zero when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().
			3. In python it takes counter as an argument (no. of instructions perform by a thread). By default semaphore counter is 1.
			4. No. of acquire() and release() need not to be matched.
		
		Bounded Semaphore: -
		-----------------
			1. It is same as semaphore but the only difference is no. of acquire() and release() need to be matched. If no. of acquire() and release() is not same then PVM will throw "ValueError: Semaphore released too many times".
		
		Barrier: -
		-------
			1. It allows multiple threads to wait on same barrier object until a predefined fixed no. of thread arrives. After arrival of fixed no. of threads, those thread are released for execution.
			2. wait() used on each thread to wait until required no. of threads arrived.
	
	Inter-thread communication: -
	--------------------------
		1. Inter-processes communication is a set of techniques for the exchange of data among multiple threads in one or more processes.
		   Inter thread communication in Python is the process of sharing data between threads. This can be done using a variety of methods, including queues,conditions, and events.
'''