"""
bank.py - Simple banking classes with inheritance and exceptions.

Learning goals:
- Create custom exceptions
- Validate inputs
- Inherit and override behavior
"""


class BalanceError(Exception):  # Define a custom exception for balance issues.
    pass  # No extra behavior is needed beyond Exception.


class BankAccount:  # Define a basic bank account class.
    def __init__(self, initial_amount, acct_name):  # Initialize account state.
        self.balance = float(initial_amount)  # Store the balance as a float.
        self.acct_name = acct_name  # Store the account name.

    def get_balance(self):  # Define a method to return the balance.
        return self.balance  # Return the current balance.

    def _validate_amount(self, amount):  # Define a helper to validate amounts.
        if amount <= 0:  # Reject non-positive amounts.
            raise ValueError("Amount must be positive")  # Raise an error for invalid amounts.

    def _ensure_funds(self, amount):  # Define a helper to check available funds.
        if self.balance < amount:  # Compare balance to requested amount.
            raise BalanceError(  # Raise a custom error if insufficient funds.
                f"Insufficient funds for {self.acct_name}. Balance: ${self.balance:.2f}"
            )  # Format the error message with account details.

    def deposit(self, amount):  # Define a deposit method.
        self._validate_amount(amount)  # Validate the deposit amount.
        self.balance += amount  # Add the amount to the balance.
        return self.balance  # Return the updated balance.

    def withdraw(self, amount):  # Define a withdrawal method.
        self._validate_amount(amount)  # Validate the withdrawal amount.
        self._ensure_funds(amount)  # Ensure the balance covers the withdrawal.
        self.balance -= amount  # Subtract the amount from the balance.
        return self.balance  # Return the updated balance.

    def transfer(self, amount, other_account):  # Define a transfer method.
        self.withdraw(amount)  # Withdraw funds from this account.
        other_account.deposit(amount)  # Deposit funds into the other account.


class InterestRewardsAcct(BankAccount):  # Define an account with interest rewards.
    def deposit(self, amount):  # Override deposit to add interest.
        self._validate_amount(amount)  # Validate the deposit amount.
        self.balance += amount * 1.05  # Add a 5 percent bonus to the deposit.
        return self.balance  # Return the updated balance.


class SavingsAcct(InterestRewardsAcct):  # Define a savings account subclass.
    def __init__(self, initial_amount, acct_name, fee=5):  # Initialize with a fee.
        super().__init__(initial_amount, acct_name)  # Initialize base attributes.
        self.fee = fee  # Store the withdrawal fee.

    def withdraw(self, amount):  # Override withdraw to include fee.
        total = amount + self.fee  # Add the fee to the withdrawal amount.
        self._validate_amount(total)  # Validate the total amount.
        self._ensure_funds(total)  # Ensure the balance covers total + fee.
        self.balance -= total  # Subtract the total from the balance.
        return self.balance  # Return the updated balance.


NOTES = """  # Store study notes as a multiline string.
Notes:
- Exceptions separate error paths from normal logic.
- Inheritance lets SavingsAcct reuse InterestRewardsAcct behavior.
- Always validate amounts to prevent negative or zero transfers.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) Why raise ValueError for non-positive amounts?
2) How does SavingsAcct change withdrawal behavior?
3) What happens if transfer calls withdraw and it raises BalanceError?
4) Where would you add logging for deposits and withdrawals?
"""


def main():  # Define the script entry point.
    dave = BankAccount(1000, "Dave")  # Create a basic account for Dave.
    sara = SavingsAcct(2000, "Sara")  # Create a savings account for Sara.

    print("Dave balance:", dave.get_balance())  # Show Dave's starting balance.
    print("Sara balance:", sara.get_balance())  # Show Sara's starting balance.

    dave.deposit(500)  # Deposit funds into Dave's account.
    sara.withdraw(300)  # Withdraw funds from Sara's account.
    print("Dave balance after deposit:", dave.get_balance())  # Show updated balance.
    print("Sara balance after withdraw:", sara.get_balance())  # Show updated balance.

    try:  # Start a protected block for a risky withdrawal.
        dave.withdraw(2000)  # Attempt to withdraw more than the balance.
    except BalanceError as exc:  # Catch insufficient funds.
        print("Withdraw failed:", exc)  # Report the error.

    dave.transfer(200, sara)  # Transfer money from Dave to Sara.
    print("Dave balance after transfer:", dave.get_balance())  # Show final balance.
    print("Sara balance after transfer:", sara.get_balance())  # Show final balance.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
