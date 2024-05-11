#! /usr/bin/python3

# Priority Scheduling (Non-preemptive Algorithm)

pid = ["P1","P2","P3","P4","P5","P6","P7"]
arrival_time = [0,2,1,4,6,5,7]
burst_time = [3,5,4,2,9,4,10]
priority = [2,6,3,5,7,4,10]


"""

Here, we sort the process according to priority. If the priority is same then sorted according to arrival time scheduling.

"""
# sorting according to arrival time, but if arrival time are same then sorting according to priority
for i in range(len(pid)):
	for j in range(i,len(pid)):
		if arrival_time[i] > arrival_time[j]:
			priority[i], priority[j] = priority[j], priority[i]
			pid[i], pid[j] = pid[j], pid[i]
			arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
		elif arrival_time[i] == arrival_time[j] and priority[i] < priority[j]:
			priority[i], priority[j] = priority[j], priority[i]
			pid[i], pid[j] = pid[j], pid[i]
			arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]

# sorting according to priority, but if priority are same then sorting according to arrival time
for i in range(1, len(pid)):
	for j in range(i, len(pid)):
		if priority[i] > priority[j]:
			priority[i], priority[j] = priority[j], priority[i]
			pid[i], pid[j] = pid[j], pid[i]
			arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
		elif priority[i] == priority[j] and arrival_time[i] > arrival_time[j]:
			priority[i], priority[j] = priority[j], priority[i]
			pid[i], pid[j] = pid[j], pid[i]
			arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
"""

Now, we apply First Come First Serve

"""

completion_time = []

for i in range(len(pid)):
	if completion_time == []:										# time completion of an initial process
		completion_time.append(arrival_time[i] + burst_time[i])
	elif completion_time[i-1] >= arrival_time[i-1]:					# if any process arrives before the completion of an initial process
		completion_time.append(completion_time[i-1] + burst_time[i])
	else:															# if any process arrives after the completion of an initial process
		completion_time.append(arrival_time[i] + burst_time[i])

turn_around_time = []
waiting_time = []

for i in range(len(pid)):
	turn_around_time.append(completion_time[i] - arrival_time[i])
	waiting_time.append(turn_around_time[i] - burst_time[i])

print("Average Turn Around Time: ",sum(turn_around_time)/len(pid))
print("Average Waiting Time: ",sum(waiting_time)/len(pid))
