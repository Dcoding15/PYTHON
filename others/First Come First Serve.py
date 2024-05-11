#! /usr/bin/python3

# First Come First Server (Non-preemtive Algorithm)

pid, arrival_time, burst_time, completion_time, turn_around_time, waiting_time = [],[],[],[],[],[]

pid = [i for i in input('Enter process ID: ').split()]

for i in range(len(pid)):
	at = int(input(f'Enter arrival time for process ID {pid[i]}: '))
	arrival_time.append(at)
	bt = int(input(f'Enter burst time for process ID {pid[i]}: '))
	burst_time.append(bt)

# sorting according to arrival time
for i in range(len(pid)):
	for j in range(i,len(pid)):
		if arrival_time[i] > arrival_time[j]:
			arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
			pid[i], pid[j] = pid[j], pid[i]

for i in range(len(pid)):
	if completion_time == []:											#time completion of an initial process
		completion_time.append(arrival_time[i] + burst_time[i])
	elif completion_time[i-1] >= arrival_time[i]:						#if any process arrives before the completion of an existing process
		completion_time.append(completion_time[i-1] + burst_time[i])
	else:																#if any process arrives after the completion of an existing process
		completion_time.append(arrival_time[i] + burst_time[i])

for i in range(len(pid)):
	turn_around_time.append(completion_time[i] - arrival_time[i])
	waiting_time.append(turn_around_time[i] - burst_time[i])


avg_turn_around_time, avg_waiting_time = 0, 0

for i in turn_around_time:
	avg_turn_around_time += (i/len(turn_around_time))

for i in waiting_time:
	avg_waiting_time += (i/len(waiting_time))

print('Average Turn Around Time:',avg_turn_around_time)
print('Average Waiting Time:',avg_waiting_time)
