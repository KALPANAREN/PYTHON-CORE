# built in namespace
"""
it contains pre-defined names of python. For ex: print, len,int, str etc. 
They live in builtins
These are used only when python can't find a name anywhere else
"""
# import builtins
# print(dir(builtins))

# global namespace
"""
each python file has it's global namespace and global namespace is shared across functions in the same file
"""
# x=10
# def greet():
#     pass

# print(globals())

# class namaspace
"""
It will store the attributes that belong to that class itself. It lives in Classname.__dict__ 
"""
# class User:
#     role = "admin"
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         return "hello"

# print(User.__dict__)

# instant namespace
"""
it contains the attributes those belong to that specific object itself
"""
# u1 = User("narendar")
# print(u1.__dict__)

# local namespace

def func():
    x=5
    return x

print(locals())