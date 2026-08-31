import time

from utils.my_decorator import log_test
from utils.my_decorator import take_screenshot_on_failure


def calculate_sum(a, b):
    """After a delay of 2 seconds, this function returns the sum of two numbers."""
    time.sleep(2)
    return a + b

def calculate_sum_with_exception(a, b):
    """After a delay of 2 seconds, this function raises a ValueError for demonstration purposes."""
    time.sleep(2)
    raise ValueError("This is a test exception for demonstration purposes.")    