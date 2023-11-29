#! /usr/bin/python3

# Round Robin Alogrithm (Preemptive)

def is_empty(arr):
	sum = 0
	for i in arr:
		sum += i
	if sum > 0:
		return True
	else:
		return False

pid, arrival_time, burst_time, completion_time, turn_around_time, waiting_time, ready_queue = ['P1', 'P2', 'P3', 'P4'],[0,1,2,4],[5,4,2,1],[],[],[],[]
gantt_chart = [arrival_time[0]]
ready_queue = [arrival_time[0]]

#time_quantum = int(input('Enter Time Quantum: '))
time_quantum = 2		#tryIn

for i in range(len(pid)):
	for j in range(i,len(pid)):
		if arrival_time[i] > arrival_time[j]:
			arrival_time[i], arrival_time[j] = arrival_time[j], arrrival_time[i]
			pid[i], pid[j] = pid[j], pid[i]
			burst_time[i], burst_time[j] = burst_time[j], burst_time[i]

#----------------------------------------------------------------

tmp = []

for i in burst_time:
	tmp.append(i)

#----------------------------------------------------------------

process_chart = []						#tryIn


for i in range(max(arrival_time)):
	

#------------------------continuation----------------------------

while(is_empty(tmp)):												# check weather sum of tmp list is 0
	for i in range(len(pid)):										# iterate i len(pid) no. of times
		if tmp[i] <= time_quantum and tmp[i] != 0:					# check weather particular element of tmp list is less than time quantum and also that element is not equal to 0
			ready_queue.append(ready_queue[i] + tmp[i])				# if condition is true then append value (ready_queue[i] + tmp[i]) in ready_queue list
			process_chart.append(pid[i])
			tmp[i] = 0												# change that element to 0 because element of that tmp list is less than and also not equal to 0
		elif tmp[i] > time_quantum:
			ready_queue.append(ready_queue[i] + time_quantum)
			process_chart.append(pid[i])
			tmp[i] -= time_quantum

#------------------------continuation----------------------------

print(ready_queue)		#tryIn
print(gantt_chart)		#tryIn
print(process_chart)	#tryIn

'''
for i in range(len(pid)):
	turn_around_time.append(completion_time[i] - arrival_time[i])
	waiting_time.append(turn_around_time[i] - burst_time[i])

avg_waiting_time, avg_turn_around_time = 0, 0

for i in waiting_time:
	avg_waiting_time += (i/len(waiting_time))
for i in turn_around_time:
	avg_turn_around_time += (i/len(turn_around_time))

print('Average Waiting Time: ',avg_waiting_time)
print('Average Turn Around Time: ',avg_turn_around_time)
'''
