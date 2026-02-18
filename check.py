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

