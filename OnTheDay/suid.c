#include <unistd.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    if (argc == 2) {
        setuid(0);
        setgid(0);
        execl("/bin/bash", "bash", "-c", argv[1], NULL);
        return 0;
    } else {
        printf("Service not available");
    }
}
