//Counting Up: Write a program that asks the user for a number and counts up from 1 to that number using a while loop.

#include<stdio.h>

int main(void) {

    int i = 1;
    int max_number;
    printf("Enter an integer between 1 and 100: ");
    scanf("%d", &max_number);

    if (max_number > 0 && max_number <= 100){
        while (i <= max_number) {
            printf("Count is at %d\n", i);
            i++;
        }
    }
    else printf("There was something wrong with your number\n");

    return 0;
}