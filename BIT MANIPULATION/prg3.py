#!/usr/bin/python3

# Check whether kth bit is 0 or 1 of a number.

def fun1(x, pos):
    if pos >= len(bin(x))-2 and pos < 0:
        return "POSITION IS OUT OF LENGTH"
    else:
        return (x & 2**pos) >> pos
print(fun1(159345, 5))
print(bin(159345))
