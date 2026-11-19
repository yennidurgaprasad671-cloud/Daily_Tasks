"""4. Bank Account System (Class, Object, Constructor)
A bank wants to manage customer accounts. Create a BankAccount class with a
constructor to initialize account number and balance. Implement methods to deposit,
withdraw, and display balance"""

class BankAccount:
    def __init__(self,accno,initial_balance=0):
        self.accno=accno
        self.balance=initial_balance
    def deposit(self,amt):
        if amt>0:
            self.balance+=amt
            print(f"Deposited Successfully {self.balance}")
        else:
            print("Enter Positive")
        
    def withdraw(self,amt):
        if amt<=self.balance:
            self.balance-=amt
            print(f"Withrdraw successsfully {self.balance}")
        else:
            print("insuffiecient Balance")
    def display_balance(self):
        print(f"Your balance is {self.balance}")
d=BankAccount(101,500)
d.deposit(300)
d.withdraw(200)
d.display_balance()
