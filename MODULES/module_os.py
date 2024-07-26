import os

# environment variable
print(os.getenv('SHELL'))

# Files and Directory
# current working directory
print(os.getcwd())


# Users and groups
# actual login name
print(os.getlogin())

# list of groups to which a user belongs.
print(os.getgrouplist('dungeonhunter',1000))

# list of supplemental group ID's
print(os.getgroups())

# Process
# current process id
print(os.getpid())

# current process group id
print(os.getpgrp())

# current process's effective group id
print(os.getegid())

# current process's real group id
print(os.getgid())

# current process's effective user id
print(os.geteuid())

# current process's real user id
print(os.getuid())

# average recent system load information
print(os.getloadavg())

# call the system call getgpid()
# run in terminal: ./process.py &
# enter pid
try:
    print(os.getpgid(8897))
except ProcessLookupError:
    print("Process is not running . . .")
