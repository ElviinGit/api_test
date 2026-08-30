import time
from functools import wraps
from .my_logger import logger


def log_test(func):
    """Decorator to log the start and end of a test function."""
    @wraps(func)
    def innner(*args, **kwargs):

        start = time.perf_counter()

        logger.info(f"[START] ---- {func.__name__}")
        try:    
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            logger.info(f"{func.__name__} | PASS  {duration:.4f} seconds)")
            return result
        except Exception as e:
            duration = time.perf_counter() - start
            logger.error(f"{func.__name__} | FAIL  {duration:.4f} seconds)")
            logger.error(f"Exception: {e}")
            raise 
    return innner

def take_screenshot_on_failure(func):
    """Decorator to take a screenshot on test failure."""
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Taking screenshot due to failure in {func.__name__}")
            # Code to take a screenshot would go here
            raise e
    return inner

#you have to complete the code in the middle


