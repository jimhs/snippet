#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <unistd.h>
#include <errno.h>

void usr1_handler(int sig_num)
{
	printf("par %d rec SIGUSR1\n", getpid());
}

int main()
{
	pid_t ret;
	int status, role = -1;

	ret = fork();

	if(ret>0) {
		printf("par %d ==\n",getpid());
		signal(SIGUSR1,usr1_handler);
		role = 0;
		pause();
		printf("par awaiting\n");
		ret = wait(&status);
	} else if (ret == 0) {
		printf("chd %d ==\n",getpid());
		role = 1;
		sleep(1);
		printf("chd sending SIGUSR1 to %d\n",getppid());
		kill(getppid(),SIGUSR1);
		sleep(2);
	} else {
		printf("par error forking: %d\n",errno);
	}

	printf("%s: exiting...\n", ( (role ==0)?"par":"chd" ));

	return 0;
}
