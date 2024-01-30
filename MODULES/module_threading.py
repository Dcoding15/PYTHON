#! /usr/bin/python3

import threading

'''
Thread class: -
------------
	Methods: -
	-------
		getName()
			Return a string used for identification purposes only. This method is deprecated, use the name attribute instead.

		isDaemon()
			Return whether this thread is a daemon. This method is deprecated, use the daemon attribute instead.

		is_alive()
			Return whether the thread is alive. This method returns True just before the run() method starts until just after the run() method terminates. See also the module function enumerate().

		join(timeout=None)
			Wait until the thread terminates. This blocks the calling thread until the thread whose join() method is called terminates -- either normally or through an unhandled exception or until the optional timeout occurs. When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof). As join() always returns None, you must call is_alive() after join() to decide whether a timeout happened -- if the thread is still alive, the join() call timed out. When the timeout argument is not present or None, the operation will block until the thread terminates. A thread can be join()ed many times. join() raises a RuntimeError if an attempt is made to join the current thread as that would cause a deadlock. It is also an error to join() a thread before it has been started and attempts to do so raises the same exception. run(self) Method representing the thread's activity. You may override this method in a subclass. The standard run() method invokes the callable object passed to the object's constructor as the target argument, if any, with sequential and keyword arguments taken from the args and kwargs arguments, respectively.

		setDaemon(daemonic)
			Set whether this thread is a daemon. This method is deprecated, use the .daemon property instead.

		setName(name)
			Set the name string for this thread. This method is deprecated, use the name attribute instead.

		start()
			Start the thread's activity. It must be called at most once per thread object. It arranges for the object's run() method to be invoked in a separate thread of control. This method will raise a RuntimeError if called more than once on the same thread object.


	Properties: -
	----------
		ident
			Thread identifier of this thread or None if it has not been started. This is a nonzero integer. See the get_ident() function. Thread identifiers may be recycled when a thread exits and another thread is created. The identifier is available even after the thread has exited.
		native_id
			Native integral thread ID of this thread, or None if it has not been started. This is a non-negative integer. See the get_native_id() function. This represents the Thread ID as reported by the kernel.
		daemon
			A boolean value indicating whether this thread is a daemon thread. This must be set before start() is called, otherwise RuntimeError is raised. Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False. The entire Python program exits when only daemon threads are left.
		name
			A string used for identification purposes only. It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor.

Timer class (child class of Thread class): -
-----------
	Methods: -
	-------
		cancel()
			Stop the timer if it hasn't finished yet.

		run()
			Method representing the thread's activity. You may override this method in a subclass. The standard run() method invokes the callable object passed to the object's constructor as the target argument, if any, with sequential and keyword arguments taken from the args and kwargs arguments, respectively.
'''
