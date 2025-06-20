//Guess the Number: Write a simple number guessing game where the user has to guess a 
//randomly generated number (between 1-10). Keep looping until they guess correctly.

#include<stdio.h>
#include<stdlib.h>

int main(void) {

    //declaring variables number for the number to guess, and guess for the users guess.
    int number, guess;
    number = rand() % 10;

    //loop through asking for a guess until the number is guessed
    while (guess != number) {
        printf("guess a number between 1 and 10: ");
        scanf("%d",&guess);
        if (guess != number) printf("Wrong, guess again\n");
    }

    //print out that the person has guessed the correct number and end the program
    printf("Correct\n");

    return 0;
}
