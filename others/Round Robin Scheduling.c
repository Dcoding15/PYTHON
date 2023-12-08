// Round Robin Scheduling

#include<stdio.h>
int isEmpty(int arr[], int size)
{
	int sum = 0;
	for (int i = 0; i < size; i++)
	{
		sum += arr[i];
	}
	if(sum > 0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
int main()
{
	int n;
	printf("Number of processes: ");
	scanf("%d",&n);
	int t;
	printf("Time quantum: ");
	scanf("%d",&t);
	int pid[n], bt[n], rq[n];
	printf("Enter values: -\n");
	printf("Process ID\tBurst Time\n");
	for(int i = 0; i < n; i++)
	{
		printf("P%d\t\t",i+1);
		pid[i] = i+1;
		scanf("%d",&bt[i]);
	}
	for(int i = 0; i < n; i++)
	{
		rq[i] = bt[i];
	}
	int a = 1;
	int gc[n*100];
	gc[0] = 0;
	while(isEmpty(rq, n))
	{
		for(int i = 0; i < n; i++)
		{
			if(rq[i] <= t)
			{
				if(rq[i] != 0)
				{
					gc[a] = gc[a-1] + rq[i];
					rq[i] = 0;
					a++;
				}
			}
			else if(rq[i] > t)
			{
				gc[a] = gc[a-1] + t;
				rq[i] -= t;
				a++;
			}
		}
	}
	int wt[a-1], tat[a-1];
	for (int i = 0; i < a-1; i++)
	{
		wt[i] = gc[i];
	}
	for (int i = 1; i < a; i++)
	{
		tat[i-1] = gc[i];
	}
	int sum_wt = 0, sum_tat = 0;
	for (int i = 0; i < a-1; i++)
	{
		sum_wt += wt[i];
		sum_tat += tat[i];
	}
	printf("Average waiting time is %f\nAverage turn around time is %f\n",(float)sum_wt/(a-1),(float)sum_tat/(a-1));
}
