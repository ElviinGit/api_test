from functools import wraps

def my_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Function starting decorating")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
        except Exception:
            a = kwargs.get("driver").isdigit()
            print(a)
            return a   
        print("Function finished decorating")   
        return result
    return inner

