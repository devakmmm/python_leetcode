"""
bank.py - Simple banking classes with inheritance and exceptions.

Learning goals:
- Create custom exceptions
- Validate inputs
- Inherit and override behavior
"""


class BalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = float(initial_amount)
        self.acct_name = acct_name

    def get_balance(self):
        return self.balance

    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

    def _ensure_funds(self, amount):
        if self.balance < amount:
            raise BalanceError(
                f"Insufficient funds for {self.acct_name}. Balance: ${self.balance:.2f}"
            )

    def deposit(self, amount):
        self._validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self._validate_amount(amount)
        self._ensure_funds(amount)
        self.balance -= amount
        return self.balance

    def transfer(self, amount, other_account):
        self.withdraw(amount)
        other_account.deposit(amount)


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self._validate_amount(amount)
        self.balance += amount * 1.05
        return self.balance


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initial_amount, acct_name, fee=5):
        super().__init__(initial_amount, acct_name)
        self.fee = fee

    def withdraw(self, amount):
        total = amount + self.fee
        self._validate_amount(total)
        self._ensure_funds(total)
        self.balance -= total
        return self.balance


NOTES = """
Notes:
- Exceptions separate error paths from normal logic.
- Inheritance lets SavingsAcct reuse InterestRewardsAcct behavior.
- Always validate amounts to prevent negative or zero transfers.
"""


QUESTIONS = """
Questions:
1) Why raise ValueError for non-positive amounts?
2) How does SavingsAcct change withdrawal behavior?
3) What happens if transfer calls withdraw and it raises BalanceError?
4) Where would you add logging for deposits and withdrawals?
"""


def main():
    dave = BankAccount(1000, "Dave")
    sara = SavingsAcct(2000, "Sara")

    print("Dave balance:", dave.get_balance())
    print("Sara balance:", sara.get_balance())

    dave.deposit(500)
    sara.withdraw(300)
    print("Dave balance after deposit:", dave.get_balance())
    print("Sara balance after withdraw:", sara.get_balance())

    try:
        dave.withdraw(2000)
    except BalanceError as exc:
        print("Withdraw failed:", exc)

    dave.transfer(200, sara)
    print("Dave balance after transfer:", dave.get_balance())
    print("Sara balance after transfer:", sara.get_balance())

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
