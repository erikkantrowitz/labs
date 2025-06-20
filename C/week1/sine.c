#include <stdio.h>
#include <math.h>

int main(void){
    double input;  //set type for input variable
    printf("Input value you would like to see sine of: ");
    scanf("%lf", &input); //ask user for input, using double for decimal reasons
    double sine =  sin(input);  //this is the math part that finds the sine of the inputed value
    printf("sine of %lf is: %lf",input,  sine); //print the result
    return 0; //end the program
}