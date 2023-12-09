# Shortest Job First (Non-preemtive)
# Note: In case of non-preemtive response time is same as waiting time.
# Here we assume that arrival time of all process is 0

n = int(input("Enter the number of processes: "))
pid, burst_time, waiting_time, turn_around_time = [], [], [], []

print("Enter values: -")
print("Processes\tBrust Time")
for i in range(n):
    p, b = map(int, input().split())
    pid.append(p)
    burst_time.append(b)

for i in range(n):
    for j in range(i, n):
        if burst_time[i] > burst_time[j]:
            burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
            pid[i], pid[j] = pid[j], pid[i]

gc = [0] * (n + 1)
for i in range(1, n + 1):
    gc[i] = gc[i - 1] + burst_time[i - 1]

waiting_time = gc[:n]
turn_around_time = gc[1:]

sum_waiting_time = sum(waiting_time)
sum_turn_around_time = sum(turn_around_time)
avg_waiting_time = sum_waiting_time / n
avg_turn_around_time = sum_turn_around_time / n

print(f"Average waiting time is {avg_waiting_time}\nAverage turn around time is {avg_turn_around_time}")

