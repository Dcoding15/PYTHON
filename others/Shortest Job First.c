// Shortest Job First (Non-Preemptive)
#include<stdio.h>
void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}
int main()
{
	int n;
	printf("Enter the number of processes: ");
	scanf("%d",&n);
	int pid[n], bt[n], wt[n], tat[n];
	printf("Enter values: -\n");
	printf("Processes\tBrust Time\n");
	for(int i = 0; i < n; i++)
	{
		scanf("%d%d",&pid[i], &bt[i]);
	}
	for(int i = 0; i < n; i++)
	{
		for(int j = i; j < n; j++)
		{
			if(bt[i]>bt[j])
			{
				swap(&bt[i], &bt[j]);
				swap(&pid[i], &pid[j]);
			}
		}
	}
    int gc[n+1];
    gc[0] = 0;    
    for (int i = 1; i < n+1; i++)
    {
        gc[i] = gc[i-1] + bt[i-1];
    }
    for (int i = 0; i < n; i++)
    {
        wt[i] = gc[i];
    }
    for (int i = 1; i < n+1; i++)
    {
        tat[i-1] = gc[i];
    }
    int sum_wt = 0, sum_tat = 0;
    float avg_wt, avg_tat;
    for (int i = 0; i < n; i++)
    {
        sum_tat += tat[i];
    }
    for (int i = 0; i < n; i++)
    {
        sum_wt += wt[i];
    }
    avg_tat = (float)sum_tat/n;
    avg_wt = (float)sum_wt/n;
    printf("Average waiting time is %f\nAverage turn around time is %f\n",avg_wt, avg_tat);
}
/*
 
 	Output: -
 	Enter the number of processes: 3
	Enter values: -
	Processes	Brust Time
	1		5
	2		4
	3		6
	Average waiting time is 4.333333
	Average turn around time is 9.333333
 
 */
