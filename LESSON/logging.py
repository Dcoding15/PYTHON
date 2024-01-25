'''
Logging: -
-------
	1. It is a way to track and record events that occur in a program. This can be helpful for debugging problems, understanding how the program is running, and collecting data about user activity.
	2. To use logging in python, import logging module.
	3. Logging data is divided into the following levels in python: -
		FATAL / CRITICAL = 50
		ERROR            = 40
		WARN / WARNING   = 30	(Default logging level)
		INFO             = 20
		DEBUG            = 10
		NOTSET           = 0

		If we don't set logger level then logging level will start from default logging level to higher level.
	4. Default file mode of log file is append.
	   Default format of log: level:name of logger:message
	5. Root logger creation using logging.basicConfig()

Problem Root Logger: -
-------------------
	1. It is a default logger.
	2. We can set basic configuration only once. After configuration we can't change.
	3. It will handle either file handler or console (any one).
	4. We can't define multiple log files.

User Logger / Customised Logger: -
-------------------------------
	1. Creation of logger object: -
		logger_name = logging.getLogger('logger name').setLevel(logging_level)
	2. Creation of handler object: -
		There are three types of handler in logging module: StreamHandler (For console), FileHandler (for file), NullHandler (for avoid of no handler found for logger).
		handler_name = logging.StreamHandler().setLevel(logging_level)
	3. Creation of formatter object: -
		formatter_name = logging.Formatter('customised format')
	4. Add formatter to handler using handler_name.setFormatter(formatter_name)
	   Add handler to logger using logger_name.addHandler(handler_name)
	5. Logging level of logger > logging level of handler ==> logging level of logger will execute
	   Logging level of logger < logging level of handler ==> logging level of handler will execute
	6. It will handle both file and stream handler at same time.
	7. We can define multiple log files.

Seperate Logger File: -
---------------------
	1. We can make separate logger configuration file and can use that file by using logging.config.fileConfig("file name")
	2. Format for logger configuration file: -
		file_name.init
		--------------
		[loggers]																<--- declare user name of loggers
		keys=root,user_logger_name1,user_logger_name2,...,user_logger_nameN		<--- declare root logger before defining user logger

		[handlers]																<--- declare user name of handlers
		keys=user_handler_name1,user_handler_name2,...,user_handler_nameN

		[formatters]															<--- declare user name of formatters
		keys=user_formater_name1,user_formater_name2,...,user_formater_nameN

		[logger_root]															<--- must define root logger with level and handlers
		level=																	<--- Logging level i.e., DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET (any one)
		handlers=																<--- must use above declared handlers

		[logger_(user_logger_name)]												<--- define user declared loggers. In the place of (user_logger_name) ==> any one declared user logger
		level=																	<--- Logging level i.e., DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET (any one)
		handlers=																<--- must use above declared handlers
		propagate=																<--- it has two value 1 means to go from current logging level to higher logging level and 0 means not to
																					 go from current logging level to higher logging level
		qualname=																<--- must use same logger name as its user_logger_name

		[handler(user_handler_name)]											<--- define user declared handlers. In the place of (user_handler_name) ==> any one declared user handler
		class=																	<--- Logger class i.e., StreamHandler, FileHandler, NullHandler (any one)
		level=																	<--- Logging level i.e., DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET (any one)
		formatter=																<--- must use above declared formatters
		args= ()																<---
		kwargs= {}																<---

		[formatter(user_formatter_name)]										<--- define user declared formatters. In the place of (user_formatter_name) ==> any one declared 
																					 user formatter
		format=																	<--- user defined format of log message
		datefmt=																<--- user defined data format of log message
		style=																	<---
		validate=																<--- it has two values True means this formatter is valid and False this formatter is not valid
		class=																	<---

Note: format values for formatters follow: https://docs.python.org/3/library/logging.html#logrecord-attributes
	  datefmt values for formatters follow: https://docs.python.org/3/library/time.html#time.strftime
'''