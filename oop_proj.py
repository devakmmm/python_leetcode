from bank import *

Dave=BankAccount(1000,"Dave")
Sara=BankAccount(2000,"Sara")

Dave.getBalance()
Sara.getBalance()   

Dave.deposit(500)
Sara.withdraw(300)

Dave.withdraw(2000)
Sara.withdraw(1000)

Dave.getBalance()
Sara.getBalance()

