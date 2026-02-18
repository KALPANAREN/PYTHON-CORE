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
print(d1._c)
print(d2._c)