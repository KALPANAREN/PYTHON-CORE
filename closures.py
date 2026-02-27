# CLOSURE IMPLEMENTATION

def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(10)
print(f(6))    # 16

print(f.__closure__)
print(f.__closure__[0].cell_contents)   # 10

# CLOSURES CAPTURE VARIABLE, NOT VALUE
def outer():
    x = 0
    def inner():
        return x
    x = 100
    return inner

f = outer()
print(f())   # 100

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

auth_logger = make_logger("AUTH")
db_logger = make_logger("DATABASE")

auth_logger("User login successful")
db_logger("Connection established")


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
