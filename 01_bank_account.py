"""

You are tasked with developing a system to manage bank accounts.
The system should allow for the following operations:
  Deposit Money: Add a specified amount of money to a bank account.
  Withdraw Money: Subtract a specified amount of money from a bank account,
  but ensure that the account balance does not become negative.
  Check Balance: Retrieve the current balance of a bank account.
See example:

account = BankAccount(100)
account.deposit(50)
print(account.check_balance())  # Prints 150

account.withdraw(30)
print(account.check_balance())  # Prints 120

account.withdraw(100)
print(account.check_balance())  # Prints 20

account.withdraw(50)  # Prints "Insufficient funds"
print(account.check_balance())  # Prints 20


Once your classes are complete, copy and paste the above example below them in order to test their functionality
"""



"""
Write a class that meets these requirements.

Name:       BankAccount

Required state:
   * balance

Behavior:
   * check_balance()      # returns the current balance
   * deposit(amount)      # adds the new amount to the balance
   * withdraw(amount)     # removes the amount from the balance, but does not allow the balance to go negative

"""

class BankAccount:
   def __init__(self, account, balance):
        self.account = account
        self.balance = balance

   def check_balance(self):
       return f"Your balance is: {self.balance}"

   def deposit(self, amount):
      self.balance += amount
      return f"You depositied {amount}. Your current account balance is {self.balance}"

   def withdraw(self, amount):
      if amount > self.balance:
         return f"Insufficient Funds. Unable to withdraw: {amount}"
      else:
         self.balance -= amount
         return f"You withdrew {amount}. Your current account balance is {self.balance}"

if __name__ == "__main__":
   account = BankAccount("12345", 100)
   print(account.check_balance())

   print(account.deposit(50))

   print(account.withdraw(30))

   print(account.withdraw(150))