#! /usr/bin/python3
# Shortest Job First (Non-preemtive)

pid = ["P1","P2","P3","P4","P5"]
arrival_time = [1,3,6,7,9]
burst_time = [7,3,2,10,8]

# sorting according to arrival time, but for same arrival time sort according to burst time
for i in range(len(pid)):
	for j in range(i+1, len(pid)):
		if arrival_time[i] > arrival_time[j]:
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
			pid[i], pid[j] = pid[j], pid[i]
			arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
		elif arrival_time[i] == arrival_time[j] and burst_time[i] > burst_time[j]:
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
			pid[i], pid[j] = pid[j], pid[i]
			arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]

# sorting according to burst time, but for same burst time sort according to arrival time
# sorting starts after index 0 because completion time of initial process is total no. of arrival and burst time
for i in range(1,len(pid)):
	for j in range(i+1, len(pid)):
		if burst_time[i] > burst_time[j]:
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
			pid[i], pid[j] = pid[j], pid[i]
			arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
		elif burst_time[i] == burst_time[j] and arrival_time[i] > arrival_time[j]:
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
			pid[i], pid[j] = pid[j], pid[i]
			arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]

completion_time = []

for i in range(len(pid)):
	if completion_time == []:											#if initial process arrives
		completion_time.append(burst_time[i] + arrival_time[i])
	elif completion_time[i-1] >= arrival_time[i]:						#if another process arrives before completion of an existing process
		completion_time.append(completion_time[i-1] + burst_time[i])
	else:																#if any process arrives after completion of an existing process
		completion_time.append(arrival_time[i] + burst_time[i])

turn_around_time = []
waiting_time = []

for i in range(len(pid)):
	turn_around_time.append(completion_time[i] - arrival_time[i])
	waiting_time.append(turn_around_time[i] - burst_time[i])

print(f"PID: {pid}")
print(f"Arrival Time: {arrival_time}")
print(f"Burst Time: {burst_time}")
print(f"Completion Time: {completion_time}")
print(f"Turn Around Time: {turn_around_time}")
print(f"Waiting Time: {waiting_time}")

sum_waiting_time = sum(waiting_time)
sum_turn_around_time = sum(turn_around_time)
avg_waiting_time = sum_waiting_time / len(pid)
avg_turn_around_time = sum_turn_around_time / len(pid)

print(f"Average waiting time is {avg_waiting_time}\nAverage turn around time is {avg_turn_around_time}")

