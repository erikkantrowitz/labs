#include <stdio.h>

int main(void) {
    char name[25];  //define string variable

    //prompt and input for name
    printf("Enter your name: ");
    scanf("%s", &name);

    //The output of hello name
    printf("Hello, %s, how are you?", name);
    return 0;
}