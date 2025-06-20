
//Given a non-negative integer n, return the factorial of n, denoted as n!. The factorial of n is defined as:

//n! = n * (n-1) * (n-2) * ... * 1

//Base case: 0! = 1


#include<stdio.h>

long int factorial(int n)
{
    //base case 0! = 1
    if (n == 1)
        return 1;
    else
      return factorial(n-1) * n;
}

int main(void)
{
    int n = 3;
  long  int result = factorial(n);
    printf("The factorial of %d is %d", n, result);
    return 0;
}

