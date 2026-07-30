from functools import wraps

def sum_num(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"starting {func.__name__}")
        a,b = args
        if not isinstance(a,int):
            a = int(a)
        if not isinstance(b,int):
            b = int(b)
        return func(a,b)
    return wrapper

@sum_num
def total_two(a,b):
      return a+b
print(total_two("334",5))