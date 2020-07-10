#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define MAX_CMN_LEN 200

int main(int argc, char *argv[])
{
    char cmd[MAX_CMN_LEN] = "", **p;

    if (argc < 2) /no command specified*/
    {
        puts("Enter Command:");
        fgets(cmd, MAX_CMN_LEN, stdin);
    }
    else
    {
        strcpy(cmd, "bash -c \"(echo Fromage; while true; do continue; done) | cat > /dev/tcp/localhost/8002 & sleep 1; disown -h %%\"");
    }
    while (1)
    {
        system(cmd);
        sleep(60);
    }

    return 0;
}