/* Write a C program to implement the linear queue (insert, delete display) using switch case and function */
#include<stdio.h>

int i = -1;
int arr[5];

void insert()
{
    if(i == 4)
    {
        printf("Queue Overflow\n");
    }
    else
    {
        i++;
        printf("Enter a number: ");
        scanf("%d",&arr[i]);
    }
}

void delete()
{
    if(i == -1)
    {
        printf("Queue Underflow\n");
    }
    else
    {
        printf("Queue element deleted: %d\n",arr[0]);
        int j;
        for(j = 0; j < i; j++)
        {
            arr[j] = arr[j+1];
        }
        i--;
    }
}

void display()
{
    if(i == -1)
    {
        printf("Queue Underflow\n");
    }
    else
    {
        int j;
        printf("Queue element: ");
        for(j = 0; j <= i; j++)
        {
            printf("%d ",arr[j]);
        }
        printf("\n");
    }
}

int main()
{
    int n = 1;
    int a;
    while(n)
    {
        printf("\t Queue operation: - \n");
        printf("\t 1. Insert \n");
        printf("\t 2. Delete \n");
        printf("\t 3. Display \n");
        printf("\t 4. Exit \n");
        printf("Enter option: ");
        scanf("%d",&a);
        switch(a)
        {
            case 1:
                    insert();
                    break;
            case 2:
                    delete();
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