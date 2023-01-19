class bank_account:
   def __init__(self):
       self.balance=0
       print("hello!!! Welcome to the deposit and withdrawal machine")
   def deposit(self):
       amount=float(input("Enter the amount to be deposited :"))
       self.balance+=amount
       print("Amount deposited",amount)
   def withdraw(self):
       amount=float(input("Enter the amount to be withdrawn :"))
       if self.balance >= amount:
           self.balance-=amount
           print("You withdrew :",amount)
       else:
           print("Insufficient balance")
   def display(self):
       print("Net available balance :",self.balance)

s= bank_account()
s.deposit()
s.withdraw()
s.display()
