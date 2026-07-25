from datetime import datetime
import time
from functools import wraps

def login_logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = datetime.now()
        print(f"Running {func.__name__}")
        print(f"Start: {start_time}")

        try:
            result = func(*args, **kwargs)
            print(result)
            return result

        except Exception as e:
            print(e)
            raise

        finally:
            stop_time = datetime.now()
            duration = (stop_time - start_time).total_seconds()
            print(f"Finished {func.__name__}")
            print(f"Duration: {duration:.2f} seconds")

    return inner


@login_logger
def login():
    time.sleep(3)
    print("Now login function is implementing")
    return "User successfully logged in!!!"

login()