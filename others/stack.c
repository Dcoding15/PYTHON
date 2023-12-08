#include<stdio.h>

int i = -1;
int arr[10];

void push()
{
    if(i == 10)
    {
        printf("Stack Overflow\n");
    }
    else
    {
        i++;
        printf("Enter a number: ");
        scanf("%d",&arr[i]);
    }
}

void pop()
{
    if(i == -1)
    {
        printf("Stack underflow\n");
    }
    else
    {
        printf("Stack removed: %d\n",arr[i]);
        i--;
    }
}

void display()
{
    int j;
    printf("Stack elements:");
    for(j = 0; j <= i; j++)
    {
        printf(" %d",arr[j]);
    }
    printf("\n");
}

int main()
{
    int n = 1;
    while(n)
    {
        printf("\t Operation for stack: - \n");
        printf("\t 	1. PUSH \n");
        printf("\t 	2. POP \n");
        printf("\t 	3. DISPLAY \n");
        printf("\t 	4. EXIT \n");
        printf("Enter your option: ");
        int a;
        scanf("%d",&a);
        switch(a)
        {
            case 1:
                    push();
                    break;
            case 2:
                    pop();
                    break;
            case 3:
                    display();
                    break;
            case 4:
                    printf("Operation ended\n");
                    n--;
                    break;
            default:
                    printf("You entered wrong option.\n");
        }
    }
}