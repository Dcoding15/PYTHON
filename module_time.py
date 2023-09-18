#! /usr/bin/python3

'''
Funtions: -
--------

asctime([tuple]) -> string
	Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'. When the time tuple is not present, current time as returned by localtime() is used.

clock_getres(clk_id) -> floating point number
	Return the resolution (precision) of the specified clock clk_id.

clock_gettime(clk_id) -> float
	Return the time of the specified clock clk_id.

clock_gettime_ns(clk_id) -> int
	Return the time of the specified clock clk_id as nanoseconds.

clock_settime(clk_id, time)
	Set the time of the specified clock clk_id.

clock_settime_ns(clk_id, time)
	Set the time of the specified clock clk_id with nanoseconds.

ctime(seconds) -> string
	Convert a time in seconds since the Epoch to a string in local time. This is equivalent to asctime(localtime(seconds)). When the time tuple is not present, current time as returned by localtime() is used.

get_clock_info(name: str) -> dict
	Get information of the specified clock.

gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)
	Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a. GMT).  When 'seconds' is not passed in, convert the current time instead. If the platform supports the tm_gmtoff and tm_zone, they are available as attributes only.

localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min, tm_sec,tm_wday,tm_yday,tm_isdst)
	Convert seconds since the Epoch to a time tuple expressing local time. When 'seconds' is not passed in, convert the current time instead.

mktime(tuple) -> floating point number

Convert a time tuple in local time to seconds since the Epoch. Note that mktime(gmtime(0)) will not generally return zero for most time zones; instead the returned value will either be equal to that of the timezone or altzone attributes on the time module.

monotonic() -> float
	Monotonic clock, cannot go backward.

monotonic_ns() -> int
	Monotonic clock, cannot go backward, as nanoseconds.

perf_counter() -> float
	Performance counter for benchmarking.

perf_counter_ns() -> int
	Performance counter for benchmarking as nanoseconds.

process_time() -> float
	Process time for profiling: sum of the kernel and user-space CPU time.

process_time_ns() -> int
	Process time for profiling as nanoseconds: sum of the kernel and user-space CPU time.

pthread_getcpuclockid(thread_id) -> int
	Return the clk_id of a thread's CPU time clock.

sleep(seconds)
	Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.

strftime(format[, tuple]) -> string
	Convert a time tuple to a string according to a format specification. See the library reference manual for formatting codes. When the time tuple is not present, current time as returned by localtime() is used.

strptime(string, format) -> struct_time
	Parse a string to a time tuple according to a format specification. See the library reference manual for formatting codes (same as strftime()).

thread_time() -> float
	Thread time for profiling: sum of the kernel and user-space CPU time.

thread_time_ns() -> int
	Thread time for profiling as nanoseconds: sum of the kernel and user-space CPU time.

time() -> floating point number
	Return the current time in seconds since the Epoch. Fractions of a second may be present if the system clock provides them.

time_ns() -> int
	Return the current time in nanoseconds since the Epoch.

tzset()
	Reinitialize the local timezone to the value stored in os.environ['TZ']. Unknown timezones will silently fall back to UTC.

Attributes: -
----------

tm_gmtoff	offset from UTC in seconds
tm_hour		hours, range [0, 23]
tm_isdst	1 if summer time is in effect, 0 if not, and -1 if unknown
tm_mday		day of month, range [1, 31]
tm_min		minutes, range [0, 59]
tm_mon		month of year, range [1, 12]
tm_sec		seconds, range [0, 61])
tm_wday		day of week, range [0, 6], Monday is 0
tm_yday		day of year, range [1, 366]
tm_year		year, for example, 1993
tm_zone		abbreviation of timezone name

Code Formats: -
------------

%Y			Year with century as a decimal number.
%m			Month as a decimal number [01,12].
%d			Day of the month as a decimal number [01,31].
%H  		Hour (24-hour clock) as a decimal number [00,23].
%M			Minute as a decimal number [00,59].
%S			Second as a decimal number [00,61].
%z			Time zone offset from UTC.
%a			Locale's abbreviated weekday name.
%A			Locale's full weekday name.
%b			Locale's abbreviated month name.
%B			Locale's full month name.
%c			Locale's appropriate date and time representation.
%I			Hour (12-hour clock) as a decimal number [01,12].
%p			Locale's equivalent of either AM or PM.

Other codes may be available on your platform.  See documentation for
the C library strftime function.
'''
