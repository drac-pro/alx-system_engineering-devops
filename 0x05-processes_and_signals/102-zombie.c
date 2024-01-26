#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int infinite_while(void);
/**
 * main - entry point
 *	creates 5 child process
 *
 * Return: 0 (success)
 */
int main(void)
{
	pid_t child;
	int i;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child != 0)
			printf("Zombie process created, PID: %d\n", child);
		else
			exit(EXIT_SUCCESS);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}

/**
 * infinite_while - loops forever
 * Return: 0 (success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
