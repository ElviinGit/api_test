from functools import wraps
from datetime import datetime
import time

def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = datetime.now()
        print(start_time)
        result = func(*args, **kwargs)
        finish_time = datetime.now()
        print(finish_time)
        return result
    return inner


def logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"Decorator  {func.__name__} start to executing")
        result = func(*args, **kwargs)
        print(f"Decorator  {func.__name__} finished")
        return result
    return inner

def retry(times):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            attempts = 0 
            while attempts < times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(e)
                    attempts += 1
            raise Exception("Too many requests")

        return inner
    return decorator
counter = 0

@retry(times=3)
@logger
@timer
def my_func():
    global counter

    counter += 1

    print(f"Attempt {counter}")

    if counter < 3:
        raise Exception("Random failure")

    print("Success!")
my_func()




