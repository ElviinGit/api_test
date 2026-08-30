import time

from utils.my_decorator import log_test
from utils.my_decorator import take_screenshot_on_failure

@log_test
def test_success():
    """A test that should pass."""
    time.sleep(1)

@log_test
@take_screenshot_on_failure
def test_failure():
    
    """A test that should fail."""
    time.sleep(1)
    raise Exception("This test is designed to fail.") 

try:
    test_failure()
except ValueError:

    pass    


