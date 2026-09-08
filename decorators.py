from functools import wraps

def my_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print("Function starting decorating")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            driver = kwargs.get("driver")
            if driver:
                driver.save_screenshot("screenshot.png")
            else:
                print("driver is not available in kwargs, cannot take screenshot.")
            raise
        print("Function finished decorating")   
        return result
    return inner