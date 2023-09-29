#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int infinite_while(void);

/**
 * infinite_while - Run an infinite while loop
 *
 * Return: Always 0 (Success)
 */

int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - Creates five zombi processes
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	pid_t pid;
	char i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			i++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
