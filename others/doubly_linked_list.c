// Write a C program to create doubly linked list

#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node * next;
	struct node * previous;
};

struct node * head;

void createNode(int val)
{
	struct node * temp = head;
	struct node * list = (struct node *)malloc(sizeof(struct node));
	if(temp->next == NULL)
	{
		temp->next = list;
		list->data = val;
		list->next = NULL;
		list->previous = temp;
	}
	else
	{
		while(temp->next != NULL)
		{
			temp = temp->next;
		}
		temp->next = list;
		list->data = val;
		list->next = NULL;
		list->previous = temp;
	}
}

void printNode()
{
	struct node * temp = head;
	while(temp != NULL)
	{
		printf("%d->",temp->data);
		temp = temp->next;
	}
	printf("NULL\n");
}

void printNodeReverse()
{
	struct node * temp = head;
	while(temp->next != NULL)
	{
		temp = temp->next;
	}
	while(temp != NULL)
	{
		printf("%d->",temp->data);
		temp = temp->previous;
	}
	printf("NULL\n");
}

int main()
{
	head = (struct node *)malloc(sizeof(struct node));
	head->next = NULL;
	head->previous = NULL;
	createNode(1);
	createNode(9);
	createNode(9);
	createNode(9);
	printNode();
	printNodeReverse();
}
