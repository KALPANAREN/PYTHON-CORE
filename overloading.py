def method_overloading(a,b):
    print(a*b)

def method_overloading(a,b,c):
    print(a*b*c)

m1 = method_overloading(3,5)
m2 = method_overloading(4,6,8)


# overloading with dispatch
from multipledispatch import dispatch

@dispatch(int,float)
def method_with_dispatch(a,b):
    print(a*b)
@dispatch(float, int,int)
def method_with_dispatch(a,b,c):
    print(a*b*c)
method_with_dispatch(2,3.5)
method_with_dispatch(3.5,7,2)
    