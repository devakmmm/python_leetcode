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

    def transfer(self, amount, otherAccount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            otherAccount.balance += amount
            print(f"\n Transferred ${amount:.2f} from {self.acctName} to {otherAccount.acctName}.\n New balance: ${self.balance:.2f} for {self.acctName}, ${otherAccount.balance:.2f} for {otherAccount.acctName}")
        except BalanceException as e:
            print(e)

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)  # 5% interest on deposit
        print(f"\n Deposited ${amount:.2f} to interest rewards account {self.acctName} with interest.\n New balance: ${self.balance:.2f}")

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee= 5  # Flat fee for withdrawals

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)  # Include fee in withdrawal check
            self.balance -= (amount + self.fee)
            print(f"\n Withdrew ${amount:.2f} with a fee of ${self.fee:.2f} from savings account {self.acctName}.\n New balance: ${self.balance:.2f}")
        except BalanceException as e:
            print(e)