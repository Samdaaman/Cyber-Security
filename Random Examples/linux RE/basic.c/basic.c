#include <stdio.h>
#include <string.h>

int main() {
    char password[20];
    while (1) {
        printf("Enter password: ");
        scanf("%s", &password);
        if (strcmp(password, "samiscool") == 0) {
            printf("yes\n");
            return 0;
        }
    }
}
