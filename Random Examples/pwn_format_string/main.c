#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
    char buf[2000];
    while (1)
    {
        read(0, buf, sizeof(buf));
        printf(buf);
    }
}