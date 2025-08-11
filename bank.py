class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.acctName = acctName
        print(f"\n Account {self.acctName} created with balance: ${self.balance:.2f}")

    def getBalance(self):
        print(f"\n Account {self.acctName} balance: ${self.balance:.2f}")   

    def deposit(self, amount):
        self.balance += amount
        print(f"\n Deposited ${amount:.2f} to account {self.acctName}.\n New balance: ${self.balance:.2f}")


    def viableTransaction(self, amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(f"\n Insufficient funds for withdrawal from account {self.acctName}. \n Current balance: ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\n Withdrew ${amount:.2f} from account {self.acctName}.\n New balance: ${self.balance:.2f}")
        except BalanceException as e:
            print(e)