from functools import wraps

def process_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"statrting {func.__name__}")
        res = func(*args, **kwargs)
        print(f"finishing {func.__name__}")
        return res
    return wrapper

@process_dec
def process():
    print("processing")
process()