#include<stdio.h>

void add(int A[],int B[], int row, int col)
{
	int C[row][col], i, j, n=0;
	for(int i=0; i<row; i++)
	{
		for(int j=0; j<col; j++)
		{
			C[i][j] = A[n] + B[n];
			n++;
		}
	}
	for(int i=0; i<row; i++)
	{
		for(int j=0; j<col; j++)
		{
			printf("%d\t",C[i][j]);
		}
		printf("\n");
	}
}

void sub(int A[],int B[], int row, int col)
{
	int C[row][col], i, j, n=0;
	for(int i=0; i<row; i++)
	{
		for(int j=0; j<col; j++)
		{
			C[i][j] = A[n] - B[n];
			n++;
		}
	}
	for(int i=0; i<row; i++)
	{
		for(int j=0; j<col; j++)
		{
			printf("%d\t",C[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	int a, b, i, j;
	scanf("%d",&a);
	scanf("%d",&b);
	int d[a*b], e[a*b];
	for(int i=0; i<a*b; i++)
	{
		scanf("%d",&d[i]);
	}
	printf("\n");
	for(int i=0; i<a*b; i++)
	{
		scanf("%d",&e[i]);
	}
	printf("\n");
	add(d,e,a,b);
	sub(d,e,a,b);
}
