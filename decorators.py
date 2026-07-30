# BASIC DECORATOR

from functools import wraps

def process_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}...")
        res = func(*args, **kwargs)
        print(f"Finished {func.__name__}.")
        return res
    return wrapper

@process_dec
def process_data():
    print("Processing data")

process_data()

# CREATE A DECORATOR TO RETURN A VALUE OF INPUTS

def value_dec(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Starting {func.__name__}...")
        a,b = args
        if not isinstance(a,int):
            a = int(a)
        if not isinstance(b,int):
            b = int(b)
        print(f"Finishing {func.__name__}...")

        return func(a,b)
    return wrapper
            
@value_dec            
def add(a, b):
    return a + b

x = add("4",5)
print(x)

# CREATE A DECORATOR

"""
Works with any function signature
Logs the function name and arguments
Multiplies the return value by 10
Still returns the correct type if the function returns None
Preserves metadata (name, docstring)
"""

from functools import wraps

def smart_dec(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Calling {func.__name__} with args = {args},kwargs = {kwargs.values()}")
        result = func(*args,**kwargs)
        print(f"Result before modification: {result}")
        if result is None:
            return None
        return 10*result
    return wrapper

@smart_dec
def add(a, b):
    return a + b
print(add(2, 3))

@smart_dec
def greet(name):
    print("Hello", name)

print(greet("Alice"))


# CREATE A DECORATOR THAT COUNTS HOW MANY TIMES A FUNCTION IS CALLED

from functools import wraps

def count_dec(func):
    count = 0
    @wraps(func)
    def wrapper(*args,**kwargs):
        nonlocal count
        count+=1
        print(f"call {count}")
        return func(*args,**kwargs)
    return wrapper
        
@count_dec
def hi():
    print("HI")
hi()
hi()
hi()

# CREATE REPETETIVE DECORATOR

from functools import wraps
def repeat(times):
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"executing {func.__name__}")
            print(func.__doc__)
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    "it is a printing function"
    print("Hi")
greet()

# CREATE A FRAMEWORK BASED DECORATOR FOR DELETING A USER

from functools import wraps

class UserRole:
    def __init__(self,name,role):
        self.username = name
        self.role = role

current_user = UserRole("Narendar","admin")

def role_decorator(req_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user is None :
                return "Authentication is required"
            if current_user.role != req_role:
                return "Forbidden: insufficient permissions"
            return func(*args, **kwargs)
        return wrapper
    return decorator

@role_decorator("admin")
def user_role():
    print("Deleted the user")
user_role()

# FLASK STYLE DECORATOR FOR ABOVE USE CASE
from functools import wraps
from flask import g, jsonify

def requires_role(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = getattr(g, "current_user", None)

            if not user:
                return jsonify({"error": "Authentication required"}), 401

            if user.role != required_role:
                return jsonify({"error": "Forbidden"}), 403

            return func(*args, **kwargs)
        return wrapper
    return decorator

# fastapi style decorator above use case

from fastapi import Depends, HTTPException, status

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role


def get_current_user():
    # normally decoded from JWT
    return User("alice", "admin")


def requires_role(required_role):
    def role_checker(user: User = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden"
            )
        return user
    return role_checker

@app.delete("/delete-user")
def delete_user(user: User = Depends(requires_role("admin"))):
    return {"status": "deleted"}

# CACHING DECORATOR

from functools import wraps

def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        print("calculating the result...")

        if key in cache:
            print("using cached value")
            return cache[key]
        
        result=func(*args, **kwargs)
        cache[key]=result
        return result
    
    return wrapper

@cache_results
def area(width, height):
    print("Computing area...")
    return width * height

print(area(width=3, height=4))
print(area(width=3, height=4))

@cache_results
def power(base, exp=2):
    print("Computing power...")
    return base ** exp

# PRACTISE DECORATOR ON FUNCTION ARGUMENTS VALIDATION

from functools import wraps
from numbers import Real
def positive_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for value in args: 
            if not isinstance(value,Real):
                raise ValueError("All numeric arguments must be numeric and positive")
        
        for value in kwargs:
            if not isinstance(value,Real):
                raise ValueError("All numeric arguments must be numeric and positive")
        
        return func(*args, **kwargs)
    return wrapper

@positive_only
def area(w, h):
    return w * h
print(area(5,-4))

######## STACKING DECORATOR ###########
"""
while calling ,if @require_auth,@log_call is the order then first log_call  wrapper is hit and next require_auth wrapper is hit
But execution starts from require_auth wrapper and executes till functional call and then enters into
log_call wrapper and executes function here.
"""
from functools import wraps
def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if user != "admin":
            raise PermissionError("Not authorized")
        print("Auth check passed")
        return func(*args, **kwargs)
    return wrapper

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@require_auth
@log_call
def delete_user(user, user_id):
    print(f"Deleting user {user_id}")
delete_user(user="admin", user_id=42)

# swapping the decorators
@log_call
@require_auth
def delete_user(user, user_id):
    print(f"Deleting user {user_id}")
delete_user(user="admin", user_id=42)