#include <stdio.h>
void f(unsigned int n)
{
	int i;
	int j;

	for (i = 0; i < n; i++)
	{
		for (j = 1; j < n; j = j * 2)
		{
			printf("[%d] [%d]\n", i, j);
		}
		printf("---\n");
	}
}
int main()
{
	f(10);
}