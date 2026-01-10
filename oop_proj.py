"""
oop_proj.py - Using the BankAccount classes from bank.py.

Learning goals:
- Import classes from another module
- Create objects and call methods
"""

from bank import BankAccount, SavingsAcct, BalanceError


def main():
    dave = BankAccount(1000, "Dave")
    sara = SavingsAcct(2000, "Sara")

    print("Dave:", dave.get_balance())
    print("Sara:", sara.get_balance())

    dave.deposit(500)
    sara.withdraw(300)
    print("Dave after deposit:", dave.get_balance())
    print("Sara after withdraw:", sara.get_balance())

    try:
        dave.withdraw(2000)
    except BalanceError as exc:
        print("Withdraw failed:", exc)

    dave.transfer(200, sara)
    print("Dave after transfer:", dave.get_balance())
    print("Sara after transfer:", sara.get_balance())


if __name__ == "__main__":
    main()
