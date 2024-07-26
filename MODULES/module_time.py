#! /usr/bin/python3

import time

'''
Funtions: -
--------

asctime([tuple]) -> string
	Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'. When the time tuple is not present, current time as returned by localtime() is used.
 	Argument tuple are (time_year, time_mon, time_mday, time_hour, time_min, time_sec, time_wday, time_yday, time_isdst)

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
tm_isdst	1 if daylight time is in effect, 0 if not, and -1 if unknown
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
%H  		        Hour (24-hour clock) as a decimal number [00,23].
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

Clock Id: -
--------
time.CLOCK_BOOTTIME				Identical to CLOCK_MONOTONIC, except it also includes any time that the system is suspended.
								This allows applications to get a suspend-aware monotonic clock without having to deal with the complications of CLOCK_REALTIME,
        						which may have discontinuities if the time is changed using settimeofday() or similar.

time.CLOCK_HIGHRES				The Solaris OS has a CLOCK_HIGHRES timer that attempts to use an optimal hardware source, and may give close to nanosecond resolution.
								CLOCK_HIGHRES is the nonadjustable, high-resolution clock.

time.CLOCK_MONOTONIC			Clock that cannot be set and represents monotonic time since some unspecified starting point.

time.CLOCK_MONOTONIC_RAW		Similar to CLOCK_MONOTONIC, but provides access to a raw hardware-based time that is not subject to NTP adjustments.

time.CLOCK_PROCESS_CPUTIME_ID	High-resolution per-process timer from the CPU.

time.CLOCK_PROF					High-resolution per-process timer from the CPU.


time.CLOCK_TAI					(International Atomic Time) The system must have a current leap second table in order for this to give the correct answer.
								PTP or NTP software can maintain a leap second table.

time.CLOCK_THREAD_CPUTIME_ID	Thread-specific CPU-time clock.

time.CLOCK_UPTIME				Time whose absolute value is the time the system has been running and not suspended, providing accurate uptime measurement, both absolute and interval.

time.CLOCK_UPTIME_RAW			Clock that increments monotonically, tracking the time since an arbitrary point, unaffected by frequency or time adjustments and not incremented while the system is asleep.

time.CLOCK_REALTIME				System-wide real-time clock. Setting this clock requires appropriate privileges.

Timezone Constants: -
------------------
time.altzone	The offset of the local DST timezone, in seconds west of UTC, if one is defined.
				This is negative if the local DST timezone is east of UTC (as in Western Europe, including the UK).
    			Only use this if daylight is nonzero.
time.daylight	Nonzero if a DST timezone is defined.
time.timezone	The offset of the local (non-DST) timezone, in seconds west of UTC (negative in most of Western Europe, positive in the US, zero in the UK). See note below.
time.tzname		A tuple of two strings: the first is the name of the local non-DST timezone, the second is the name of the local DST timezone.
				If no DST timezone is defined, the second string should not be used.
'''
