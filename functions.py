# ORDERING RULE--VERY VERY IMP
def func(positional, default=10, *args, **kwargs):
    pass

# positional args
def sub(a, b):
    return a - b
sub(5, 2)

# keyword args
sub(b=2, a=5) # passing order doesn't matter

# variable length arguments
def total(*args):
    return sum(args) # args is tuple


def arg_nums(*args):
    for num in args:
        print(num)
    
arg_nums([1,3,4,5,6])

def kwargs_data(**args):
    for key,value in args.items():
        print(f"{key}:{value}")
kwargs_data(name='Kalpa', age= 32, band ='TE02', location= 'India')

def args_kwargs(*args,**kwargs):
    for ele in args:
        print(ele)
    for key,value in kwargs.items():
        print(key,value)
args_kwargs(1,3,4,5,6,"Kalpa Narendar Reddy",name='Kalpa', age= 32, band ='TE02', location= 'India')

###### CLOSURES ############

def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(10)
print(f(5))  # 15

# closure is saved in cell object
f = outer()
print(f.__closure__)
print(f.__closure__[0].cell_contents)

# modifying closure variables
def outer():
    x = 10
    def inner():
        x += 1  # UnboundLocalError
    inner()

def outer():
    x = 10
    def inner():
        nonlocal x  # with nonlocal we can modify them
        x += 1
        print(x)
    inner()

# closures as function factories
def power(n):
    def inner(x):
        return x ** n
    return inner

square = power(2)
cube = power(3)

print(square(5))  # 25
print(cube(5))    # 125
