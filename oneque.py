# HAPPY NUMBER(the no where the sum of digits sqauares upon)
class BankAccount():
    def __init__(self,owner,balance=0):
        self.ac_holder = owner
        self.total_bal = balance
    def deposit(self,dep_amount):
        self.total_bal+=dep_amount
        print(f"{dep_amount} is deposited into account")
        print(f"the final balance in {self.ac_holder}'s account is {self.total_bal}")
    def withdraw(self,wd_amt):
        self.total_bal_=wd_amt
        print(f"{wd_amt} is withdwan")
        print(f"the final balance in {self.ac_holder}'s account is {self.total_bal}")

ac1 = BankAccount("Narendar",100)
ac1.deposit(1000)
ac1.withdraw(250)

