# Python Beginner Challenge 2: Number Pattern Printer
#
# Objective: Write a program that prints a simple number pattern using loops.
# Specifically, print a right-angled triangle of numbers where each row contains
# numbers from 1 to the row number.
#
# Example output for 5 rows:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# Requirements:
# - Ask the user for the number of rows (use input, convert to int).
# - Use nested loops: outer loop for rows, inner loop for numbers in each row.
# - Print numbers on the same line for each row, separated by spaces.
# - Use print() with end=' ' for same line, and print() alone for new line.
# - Handle invalid input (non-positive numbers) with a message.
#
# Hints:
# - Outer loop: for row in range(1, rows+1):
# - Inner loop: for num in range(1, row+1):
# - Print: print(num, end=' ')
# - After inner loop: print()  # new line
#
# This challenge covers: Input/Output, Loops, Basic Operations.
#
# Write your code below this comment block.

# Your code here
try:
    rows = int(input("Insert the number of rows: "))
    if rows < 0:
        print("Negative numbers are invalid")
    i= 1
    for i in range(1, rows+1):
        print()
        for j in range(i):
            print(j+1, end=" ")
    print()
except TypeError:
    print