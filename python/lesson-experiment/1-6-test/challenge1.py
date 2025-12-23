# Python Beginner Challenge 1: Simple Calculator
#
# Objective: Create a simple calculator program that takes two numbers and an operation from the user,
# performs the calculation, and displays the result.
#
# Requirements:
# - Use input() to get two numbers (as floats) and an operation (+, -, *, /). x
# - Use variables to store the inputs and result. x
# - Use conditional logic (if/elif/else) to determine which operation to perform. x
# - Handle division by zero with an appropriate message. x
# - Display the result using print(). x
# - Test with different operations and edge cases. x
#
# Hints:
# - Convert inputs: num1 = float(input("Enter first number: "))
# - Operation: op = input("Enter operation (+, -, *, /): ")
# - Conditionals: if op == '+': result = num1 + num2
# - For division: if num2 != 0: result = num1 / num2 else: print("Cannot divide by zero")
#
# This challenge covers: Variables, Data Types, Basic Operations, Input/Output, Conditional Logic.
#
# Write your code below this comment block.

# Your code here

# making operations a global set of symbols, this way I can easily add or remove some later
OPERATIONS = ['+', '-', '*', '/']

class Calculator:
    def __init__(self):
        pass

    # top level I am puting the operation methods so they are easy to find and change/ add to it later to add more functionality
    def add(self):
        self.result = self.num1 + self.num2

    def subtract(self):
        self.result = self.num1 - self.num2

    def divide(self):
        if self.num2 == 0:
            self.result = "Cannot divide by 0"
        else:
            self.result = self.num1 / self.num2

    def mult(self):
        self.result = self.num1 * self.num2
        
    def calc_logic(self):

        # this is a really cool way to do this, I should try and do things this way more often.
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.mult,
            '/': self.divide
        }

        if self.operator in operations:
            operations[self.operator]()

        # This line shouldn't ever execute, the other validation should catch it before it gets here, but just in case
        else:
            print("something went wrong, sorry")

    # These Methods are largely static, should not need to modify them much if at all to add functionality  
    def get_user_input(self):
        # TODO add validation for inputs
        self.num1 = float(input("Enter your first number: "))
        self.num2 = float(input("Enter your second number: "))
        # loop to continue asking for an operation symbol until you get a valid one
        valid = False
        while not valid:
            self.operator = input(f"Enter operation ({OPERATIONS}): ")
            if self.operator in OPERATIONS:
                valid = True
            else:
                print("I didn\'t understand that, try a valid symbol")

    def print_result(self):
        print(f"The result is: {self.result}")

if __name__ == "__main__":
    run = Calculator()

    run.get_user_input()
    run.calc_logic()
    run.print_result()


# What I learned here:
# Got quite a few reps on Object Oriented Design
# I have a better understanding of class sturcture and encapsulating 
# I learned about handling data inside a class, its way simpler than dealing with figuring out return values especially when dealing with 
# functions/methods that need to return multiple variables