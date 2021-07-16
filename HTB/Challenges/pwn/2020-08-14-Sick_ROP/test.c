#include <unistd.h>

int main() {
    execve("/bin/sh", 0x0, 0x0);
}