class ATM():
  def __init__(self):
    self.balance=0
  def check_balance(self):
    return self.balance
  def deposit(self,amount):
    self.balance=self.balance+amount
    return f"The {amount} is deposited.Thus new balance is {self.balance}."
  def withdraw(self,amount):
    if self.balance>=amount:
        self.balance=self.balance-amount
        return f"The {amount} is withdrawn.thus the new balance is {self.balance}."
    else:
        return f"Not sufficient balance."  

        
atm=ATM()
print(atm.check_balance())
print(atm.deposit(1000))
print(atm.withdraw(50))
print(atm.withdraw(100))
print(atm.withdraw(850))
print(atm.withdraw(50))
