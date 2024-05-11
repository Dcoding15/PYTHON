#!/usr/bin/python3.11

from socket import gethostbyname, socket, AF_INET, SOCK_STREAM, gaierror, error
from subprocess import call
from sys import exit
from datetime import datetime

call('clear',shell=True)                                # Clear your terminal screen

remote_server = input("Enter a remote host to scan: ")  # Input of remote server name
remote_host = gethostbyname(remote_server)              # Input of remote hostname

print(f"Scanning remote host : {remote_host}")          # Print value of remote hostname

pre_scanning_date_time = datetime.now()                 # Input of pre scanning date and time

try:
    for port in range (1,5000):
        s = socket(AF_INET, SOCK_STREAM)
        res = s.connect_ex((remote_host, port))
        if res == 0:
            print(f"{port} : PORT OPENED")
        s.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    exit();
except gaierror:
    print("Hostname could not be resolved . . .")
    exit()
except error:
    print("Could not connect to server . . .")
    exit()

post_scanning_date_time = datetime.now()                # Input of post scanning date and time
total_timing = post_scanning_date_time - pre_scanning_date_time
print(f"Scanning completed in {total_timing}")