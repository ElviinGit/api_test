from functools import wraps
from utils.logger import my_logger

def my_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        my_logger.info("Function starting decorating")
        my_logger.info(f"args: {args}")
        my_logger.info(f"kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            driver = kwargs.get("driver")
            if driver:
                driver.save_screenshot("screenshot.png")
            else:
                my_logger.error("driver is not available in kwargs, cannot take screenshot.")
            raise
        my_logger.info("Function finished decorating")   
        return result
    return inner