class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("HELLO!!!WELCOME TO THE DEPOSIT & WITHDRAWL MACHINE")

    def deposit(self):
        amount = float(input("Enter the amount to be deposited:"))
        self.balance += amount
        print("\n deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter the amount to be withdraw:"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n withdraw:", amount)
        else:
            print("\n insufficient balance")

    def display(self):
        print("\n net available:", self.balance)


s = Bank_Account()
s.deposit()
s.withdraw()
s.display()
