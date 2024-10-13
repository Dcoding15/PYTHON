#!/usr/bin/python3

# Find non-repeating element from the list

def fun1(lists):
    ans = 0
    for i in lists:
        ans ^= i
    return ans

l = [1, 2, 3, 4, 3, 2, 1]
print(fun1(l))
