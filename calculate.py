from functools import wraps
from datetime import datetime
import time
def log_test(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = datetime.now()
        try:
            print(f"Test '{func.__name__}' started at {start_time}")
            result = func(*args, **kwargs)
            end_time = datetime.now()
            print(f"Test '{func.__name__}' ended at {end_time}")
            print(f"Duration: {end_time - start_time}")
            return result
        except Exception as e:
            end_time = datetime.now()
            print(f"Test '{func.__name__}' ended at {end_time}")
            print(f"Duration: {end_time - start_time}")
            print(f"Test '{func.__name__}' failed with exception: {e}")
            raise
    return inner

@log_test
def test_myfunc():
    time.sleep(1)  # Simulate some work
    raise Exception("This is a test exception")

test_myfunc()
    

