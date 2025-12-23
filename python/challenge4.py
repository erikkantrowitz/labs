# Python OO Challenge: Simple Bank Account System
#
# Objective: Create a simple bank account system using Object-Oriented Programming (OOP) concepts. This will introduce you to classes, objects, attributes, and methods in Python.
#
# Requirements:
# - Define a BankAccount class with an initial balance (default to 0).
# - Implement a deposit method that adds money to the balance.
# - Implement a withdraw method that subtracts money from the balance (check for sufficient funds).
# - Implement a get_balance method that returns the current balance.
# - In the main part of the program, create a BankAccount object, perform some deposits and withdrawals, and print the balance.
#
# Hints:
# - Use __init__ to initialize the class with balance.
# - Methods should use self to access attributes.
# - For withdraw, check if balance >= amount before subtracting.
# - Use input() to make it interactive if you want, but start simple.
#
# Bonus: Add interest calculation or multiple accounts.
#
# Write your code below this comment block.

# Your code here

# Let's start with the class definition
class BankAccount:
    # The __init__ method is called when you create a new object (instance) of the class
    # It sets up the initial state of the object
    def __init__(self, initial_balance=0):
        # self.balance is an attribute (variable) that belongs to the object
        self.balance = initial_balance

    # A method to deposit money
    def deposit(self, amount):
        try: 
            self.check_valid(amount)
            self.balance += amount
            print(f"Deposited ${amount}  Your balance is now {self.get_balance()}")
        except(ValueError, TypeError) as e: 
            print(f"Invalid deposit: {e}")

    # A method to withdraw money
    def withdraw(self, amount): 
        try:
            self.check_valid(amount)
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}.  Your balance is now ${self.get_balance()}")
            else:
                print("There was not enough in the account, add money before trying again")
        except(ValueError, TypeError) as e:
            print(f"Invalid deposit: {e}")

    # A method to get the current balance
    def get_balance(self):
        return self.balance
    
    def check_valid(self, amount):
        if amount <= 0: 
            raise ValueError("Amount must be positive") 
        elif not isinstance(amount, (int,float)): 
            raise TypeError("can only accept integers and floats") 
        else:
            return True

# Now, let's use the class (this is outside the class definition)
if __name__ == "__main__":
    # Create a new bank account with initial balance of 100
    my_account = BankAccount(100)
    
    # Perform some operations
    my_account.deposit(-50)
    my_account.withdraw("f")
    my_account.withdraw(30)
    my_account.withdraw(150)  # This should fail
    
    # Print the final balance
    print(f"Final balance: ${my_account.get_balance()}")