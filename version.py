from functools import wraps
import time


def retry(times):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            attempts = 0
            while attempts < times:
                try: 
                    print(f"Attempts {attempts + 1}/{times}")
                    result = func(*args, **kwargs)
                    print(result)
                    return result
                except Exception as e:
                    print(e)
                    attempts +=1
            raise Exception("All retry is is spent")   
        return inner
    return decorator

counter = 0
@retry(times=5)
def login():
    time.sleep(1)
    global counter
    counter += 1    
    if counter < 100:
        raise Exception("There was a issues temprorarly, try more")   
    print("login start to print")
    return "You're almost logged in bro!"


login()
