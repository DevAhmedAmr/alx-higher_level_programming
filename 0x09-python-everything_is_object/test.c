#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void function(char *str);

int main(void)
{
	int str = 1;
	printf("%p\n", &str);
	str = 2;
	printf("%p\n", &str);

	return 0;
}

void function(char *str)
{
	strcpy(str, "Hello World!\n");
	printf("in - %s\n", str);
}