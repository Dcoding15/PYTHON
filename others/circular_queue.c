// Write a C program to implement the circular queue (enqueue, dequeue and display) using switch case and function
#include<stdio.h>

int high = -1, low = -1;
int arr[5];

void enqueue()
{
	if((high + 1) % 5 == low)
	{
		printf("Circular Queue Overflow\n");
	}
	else if(high == -1 && low == -1)
	{
		high = 0; low = 0;
		printf("Enter a number: ");
		scanf("%d",&arr[high]);
	}
	else
	{
		high = (high + 1) % 5;
		printf("Enter a number: ");
		scanf("%d",&arr[high]);
	}
}

void dequeue()
{
	if(low == -1 && high == -1)
	{
		printf("Circular Queue Underflow\n");
	}
	else if(low == high)
	{
		printf("Element deleted: %d\n",arr[low]);
		low = -1; high = -1;
	}
	else
	{
		printf("Element deleted: %d\n",arr[low]);
		low = (low + 1) % 5;
	}
}

void display()
{
	if(low == -1 && high == -1)
	{
		printf("Circular Queue Underflow\n");
	}
	else
	{
		int j;
		printf("Queue elements: ");
		for(j = low; j != high; j = (j+1) % 5)
		{
			printf("%d ",arr[j]);
		}
		printf("%d ",arr[j]);
		printf("\n");
	}
}

int main()
{
    int n = 1, a;
    while(n)
    {
        printf("\t Queue operation: - \n");
        printf("\t 1. Enqueue \n");
        printf("\t 2. Dequeue \n");
        printf("\t 3. Display \n");
        printf("\t 4. Exit \n");
        printf("Enter option: ");
        scanf("%d",&a);
        switch(a)
        {
            case 1:
                    enqueue();
                    break;
            case 2:
                    dequeue();
                    break;
            case 3:
                    display();
                    break;
            case 4:
                    n--;
                    printf("Operation ended\n");
                    break;
            default:
                    printf("You entered wrong choice\n");
        }
    }
}