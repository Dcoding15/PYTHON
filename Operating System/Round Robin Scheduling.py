#! /usr/bin/python3

# Round Robin Scheduling (Preemptive Algorithm)

from sys import maxsize
arrival_time = []
burst_time = []
waiting_time = []
completion_time = []
turn_around_time = []
pid = []
time_quantum = 5
tmp = []

# For user input purpose
#time_quantum = int(input("Enter Time Quantum: "))
#pid = [i for i in input("Enter Process ID: ").split()]
#arrival_time = [int(i) for i in input("Enter Arrival Time: ").split()]
#burst_time = [int(i) for i in input("Enter Burst Time: ").split()]

no_of_processes = len(pid)
indx = -1
time = 0
s = [[-1 for j in range(20)] for i in range(no_of_processes)]
a, b, c = [], [], no_of_processes
for i in range(no_of_processes):
    b.append(burst_time[i])
    a.append(arrival_time[i])
start_time = [[0 for _ in range(2)] for _ in range(no_of_processes)]

#------------------------code starts from below-----------------------------------------
while(c != 0):
    mini = maxsize
    flag = False
        for i in range(no_of_processes):
        if a[i] <= time and mini > a[i] and b[i] > 0:
            indx = i
            mini = a[i]
            flag = True

    if not flag:
        time += 1
        continue

    j = 0

    if s[indx][j] != 1:
        j += 1

    if s[indx][j] == -1:
        s[indx][j] = time
        start_time[indx][j] = time

    if b[indx] <= time_quantum:
        time += b[indx]
        b[indx] = 0
    else:
        time += time_quantum
        b[indx] -= time_quantum

    if b[indx] > 0:
        a[indx] = time + 0.01

    if b[indx] == 0:
        c -= 1
        completion_time.append(time)
        tmp.append(indx+1)


for i in range(no_of_processes):
    for j in range(i, no_of_processes):
        if tmp[i] > tmp[j]:
            tmp[i], tmp[j] = tmp[j], tmp[i]
            completion_time[i], completion_time[j] = completion_time[j], completion_time[i]

for i in range(len(completion_time)):
    turn_around_time.append(completion_time[i] - arrival_time[i])
    waiting_time.append(turn_around_time[i] - burst_time[i])

print("Average Waiting Time:",sum(turn_around_time)/no_of_processes)
print("Average Turn Around Time:",sum(waiting_time)/no_of_processes)
