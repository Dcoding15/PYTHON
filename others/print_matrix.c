#include<stdio.h>
int main()
{
	int row, col, m, n;
	printf("Enter row: ");
	scanf("%d",&m);
	printf("Enter column: ");
	scanf("%d",&n);
	int A[m][n];
	printf("Enter matrix elements: -\n");
	for(row=0; row<m; row++)
	{
		for(col=0; col<n; col++)
		{
			scanf("%d",&A[row][col]);
		}
	}
	printf("Entered matrix: -\n");
	for(row=0; row<m; row++)
	{
		for(col=0; col<n; col++)
		{
			printf("%d\t",A[row][col]);
		}
		printf("\n");
	}
}
