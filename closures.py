
# CLOSURE IMPLEMENTATION
"""A function becomes a closure when both of these conditions are true:\
1) It is a nested function.
2) It captures (references) a variable from its enclosing scope, 
and that enclosing scope has already finished executing when the nested function is later called. """

# let us first see why something is not closure and then move to closure

# NON-CLOSURE

def outer():
    x = 10
    def inner():
        return x
    print(inner())

result = outer() # 10
print(result) # None

# CLOSURE

def outer():
    x = 10
    def inner():
        return x
    return inner

result = outer()
print(result) # <function outer.<locals>.inner at 0x000001EC5B1C2200>

# AN EXAMPLE

def outer(x):
    def inner(y):
        return x + y
    return inner

addfunc = outer(10)
print(addfunc(6))    # 16

print(addfunc.__closure__)
print(addfunc.__closure__[0].cell_contents)   # 10

# CLOSURES CAPTURE VARIABLE, NOT VALUE

def outer():
    numbers = [1, 2]

    def inner():
        return numbers

    numbers.append(3)
    numbers.append(4)

    return inner

f = outer()
print(f())

# MODIFYING THE CAPTURED VARIABLE using nonlocal

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

c = counter()
print(c())  # 1
print(c())  # 2

### CLOSURES AS FUNCTION FACTORIES  ###

def make_logger(prefix):
    def log(message):
        print(f'{prefix} {message}')
    return log

auth_logger = make_logger("AUTH") # <function make_logger.<locals>.log at 0x000002C123BA6200>
db_logger = make_logger("DATABASE") # <function make_logger.<locals>.log at 0x000002C123BA6290>

auth_logger("User login successful") # AUTH User login successful
db_logger("Connection established") # DATABASE Connection established


def make_api_caller(base_url, api_key):
    def call(endpoint):
        print(f"Calling {base_url}/{endpoint} with key={api_key}")
        # here you would normally send a request
    return call

github_api = make_api_caller("https://api.github.com", "GITHUB_KEY")
weather_api = make_api_caller("https://api.weather.com", "WEATHER_KEY")

github_api("users/octocat")
weather_api("forecast/today")

print(github_api.__closure__)
