// Write a C program to create circular linked list

#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node * next;
};

struct node * head;

void createNode(int val)
{
	struct node * temp = head;
	struct node * list = (struct node *)malloc(sizeof(struct node));
	if(temp->next == head)
	{
		temp->next = list;
		list->next = head;
		list->data = val;
	}
	else
	{
		while(temp->next != head)
		{
			temp = temp->next;
		}
		temp->next = list;
		list->next = head;
		list->data = val;
	}
}

void printNode(int n)
{
	struct node * temp = head;
	int range = 1;
	while(range != n)
	{
		temp = temp->next;
		if(temp == head)
		{
			temp = temp->next;
		}
		printf("%d->",temp->data);
		range++;
	}
	printf("%d\n",temp->next->data);
}

int main()
{
	head = (struct node *)malloc(sizeof(struct node));
	head->data = 0;
	head->next = head;
	createNode(1);
	createNode(2);
	createNode(3);
	createNode(4);
	createNode(5);
	createNode(6);
	createNode(7);
	createNode(8);
	createNode(9);
	printNode(100);
}
