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

g1 = GrandParent(2400)
print(g1.asset1)
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

######  ENCAPSULATION IN OOPS    ##########

# PRIVTE MEMBERS

class Base:
    def __init__(self):
        self.a = 40
        self.__b = 30
class Child(Base):
    def __init__(self):
        super().__init__()
o1 = Base()
print(o1.a)
print(o1.__b)   # AttributeError: 'Child' object has no attribute '__b'
o2 = Child()
print(o2.__b)   # AttributeError: 'Child' object has no attribute '__b'

class BankAccount():
    def __init__(self,bal):
        self.__balance = bal
    def deposit(self, amt):
        self.__balance+=amt
    def withdraw(self, amt):
        if self.__balance>amt:
            self.__balance-=amt
        else:
            print("insufficient balance")
    def getbalance(self):
        return self.__balance

b = BankAccount(1000)
b.deposit(200)
print(b.getbalance())
b.withdraw(800)
print(b.getbalance())
print(b.__balance)

# PROTECTED MEMBERS

class Base:
    def __init__(self):
        self._c = 10
class Children(Base):
    def __init__(self):
        self._c = 5676
d1 = Base()
d2 = Children()
print(d1._c)    # 10
print(d2._c)    # 5676

# METHOD OVERRIDING

class Vehicle:
    def __init__(self, brand,speed):
        self.brand = brand
        self.speed = speed
    def display_info(self):
        print(f"The car info is: {self.brand} company and runs at {self.speed}")

class Car(Vehicle):
    def __init__(self, brand,speed,fuel_type):
        super().__init__(brand,speed)
        self.fuel_type = fuel_type
    def display_info(self):
        print(f"The car info is: {self.brand} company and runs at {self.speed} and uses {self.fuel_type}")

v1 = Vehicle("BMW",200)
c1 = Car("BMW",200,"diesel")
c1.display_info()

# PRACTISE PROBLEM FOR SUPER()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary} per month")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        super().show_details()
        print(f"Department: {self.department}")

e1 = Employee("Naren", 100000)
m1 = Manager("Ankit", 1000000, "Google DM")

e1.show_details()
print("-----")
m1.show_details()

# 
import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        base_area = super().area()   # from Shape
        return base_area + (self.length * self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        base_area = super().area()   # from Shape
        return base_area + (math.pi * self.radius ** 2)

shapes = [
    Rectangle(5, 3),
    Circle(2.5),
    Shape()
]

for shape in shapes:
    print(type(shape).__name__, "area =", shape.area())

class Payment:
    def __init__(self,amount):
        self.amount = amount
        
    def pay(self):
        print(f"pay the {self.amount}")

class CreditCardPayment(Payment):
    def pay(self):
        print(f"this is credit card payment,pay outstanding of {self.amount}")

class PayPalPayment(Payment):
    def pay(self):
        print(f"this is PayPal Payment, do this {self.amount} in PayPal app")

class UPIPayment(Payment):
    def pay(self):
        print(f"this is UPI Payment, please transact {self.amount}")

objs = [Payment(1000),CreditCardPayment(3000),PayPalPayment(500),UPIPayment(700)]
res = [obj.pay() for obj in objs]

# 
class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount
    
    def get_discounted_price(self):
        return self.price * (100 - self.discount) / 100

class Electronics(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 10)

class Clothing(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 20)

class Groceries(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 5)

e1 = Electronics("washing machine", 30000)
print(e1.get_discounted_price())

# METHOD RESOLUTION ORDER(MRO)

class A:
    def who(self):
        print("A")

class B(A):
    def who(self):
        print("B")

class C(A):
    def who(self):
        print("C")

class D(B, C):
    pass
d = D()
d.who()
print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# mro in case of super()
"""
super() does NOT mean “call my parent class”.
👉 It means “call the next class in the MRO after B”.
"""
class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        print("B start")
        super().greet()
        print("B end")

class C(A):
    def greet(self):
        print("C start")
        super().greet()
        print("C end")

class D(B, C):
    pass
d = D()
d.greet()

######### ABSTRACT CLASS    ################

# let us first see a normal use case
class Vehicle:

    def start(self):
        pass
    def stop(self):
        pass

class Car(Vehicle):
    pass

c = Car()
c.start() # nothing happens and no error technically but we used a method that does nothing..meaningless

# using abstract 
from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        """
        ABC with abstractmethod enforces the child class to use the method. If we don't mention the child(ABC)
        the abstract method doesn't make any meaning
        """
        pass

class Car(Vehicle):
    pass

c= Car() # raise an error since we have not used start method in the Car. ABC with abstractmethod enforces the child class to use the method

from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class Razorpay(PaymentGateway):

    def pay(self, amount):
        print("Razorpay payment")

    def refund(self, amount):
        print("Refund")

# child can override abstact method similar to normal methods
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        print("Preparing to speak...")

class Dog(Animal):

    def speak(self):
        super().speak()
        print("Woof")