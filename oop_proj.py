"""
oop_proj.py - Using the BankAccount classes from bank.py.

Learning goals:
- Import classes from another module
- Create objects and call methods
"""

from bank import BankAccount, SavingsAcct, BalanceError  # Import classes and exception.


def main():  # Define the script entry point.
    dave = BankAccount(1000, "Dave")  # Create a basic account for Dave.
    sara = SavingsAcct(2000, "Sara")  # Create a savings account for Sara.

    print("Dave:", dave.get_balance())  # Print Dave's starting balance.
    print("Sara:", sara.get_balance())  # Print Sara's starting balance.

    dave.deposit(500)  # Deposit money into Dave's account.
    sara.withdraw(300)  # Withdraw money from Sara's account.
    print("Dave after deposit:", dave.get_balance())  # Show Dave's updated balance.
    print("Sara after withdraw:", sara.get_balance())  # Show Sara's updated balance.

    try:  # Start a protected block for a risky withdrawal.
        dave.withdraw(2000)  # Attempt to withdraw too much.
    except BalanceError as exc:  # Catch the insufficient funds error.
        print("Withdraw failed:", exc)  # Print the error message.

    dave.transfer(200, sara)  # Transfer funds from Dave to Sara.
    print("Dave after transfer:", dave.get_balance())  # Show Dave's final balance.
    print("Sara after transfer:", sara.get_balance())  # Show Sara's final balance.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- dave = BankAccount(1000, "Dave"):
  creates a basic account with 1000.0.
- sara = SavingsAcct(2000, "Sara"):
  creates a savings account with 2000.0.
- dave.deposit(500):
  updates Dave to 1500.0.
- sara.withdraw(300):
  withdraws 300 plus the savings fee.
- try/except around dave.withdraw(2000):
  catches BalanceError for insufficient funds.
- dave.transfer(200, sara):
  moves 200 from Dave to Sara.
- print balances:
  outputs the final balances for both accounts.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
