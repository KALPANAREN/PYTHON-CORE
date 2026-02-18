# basic class definition and instance variables and methods
class Employee():
    hike_para = 0.1
    def __init__(self,name:str,age,salary):
        self.f_name = name.split()[0]
        self.l_name = name.split()[1]
        self.age = age
        self.pay = salary

    def email_id(self):
        return f'{self.f_name+self.l_name+'@globalogic.com'}'
    
    def hike(self):
        self.pay = self.pay+self.pay*self.hike_para
        return self.pay

e1 = Employee("Narendar Reddy",34,130000)
e2 = Employee("Chilukoti Nagababu",34,128000)
print(e1.f_name)
print(e1.hike())

######### CLASS METHOD #########

class Manager():
    hike_para = 0.15
    def __init__(self,name:str,client,no_of_proj,place):
        self.f_name = name.split()[0]
        self.l_name = name.split()[1]
        self.client = client
        self.location = place
        self.total_proj = no_of_proj
    @classmethod
    def new_hike(cls,new_rate):
        cls.hike_para = new_rate

m1 = Manager("Prashant Kumar",'google',3,"hyderabad")
m1.new_hike(0.2)
print(m1.hike_para)

####### INHERITANCE ###########

class Employee():
    hike_para = 0.1
    def __init__(self,name,age,salary):
        self.f_name = name.split()[0]
        self.l_name = name.split()[1]
        self.age = age
        self.pay = salary
        return self

    def email_id(self):
        return f'{self.f_name+self.l_name+'@globalogic.com'}'
    
    def hike(self):
        self.pay = self.pay+self.pay*self.hike_para
        return self.pay
    
class Developer(Employee):
    
    def __init__(self, name, age, salary,prog_lang):
        super().__init__(name, age, salary)
        self.lang = prog_lang

    
d1 = Developer("Narendar Reddy",34,130000,'python')
print(d1.hike())


# use 3 classes for initialising variables in one class, calcuation in one class and display results in another class

class GrandParent():
    def __init__(self,a1,a2):
        self.asset1 = a1
        self.asset2 = a2

class Parent(GrandParent):
    def calc(self):
        self.asset3 = self.asset1+self.asset2
        return self.asset3

class Children(Parent):
    def enjoy(self):
        print(f'{self.calc()} is mine')

g1 = GrandParent()
c1 = Children(10000,22000)
print(g1.asset1)
c1.enjoy()

# create a bank account class to display balance after transactions

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