#define _GNU_SOURCE
#include <linux/fcntl.h>
#include <unistd.h>

int main() {
    execveat(0x0, "/bin/sh", 0x0, 0x0);
}