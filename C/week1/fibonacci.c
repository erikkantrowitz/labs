/*
Given a number n, return the nth Fibonacci number using recursion. The Fibonacci sequence is defined as:

fib(0) = 0

fib(1) = 1

fib(n) = fib(n-1) + fib(n-2) for n > 1

*/
#include<stdio.h>

int fibonacci(int n)
{
    if (n <= 1)
        return n;
    else    
        return fibonacci(n-1) + fibonacci(n-2);
}
int fibonacci_ternary(int n)
{
   return  n<=1 ?  n : fibonacci_ternary(n-1) + fibonacci_ternary(n-2);
}

int main(void) 
{
    int n;
    int result;
    printf("Enter the number you would like: \n");
    scanf("%d", &n);

//    result =  fibonacci(n);
    result = fibonacci_ternary(n);
    printf("the %d fibonacci number is: %d\n", n,result);
}