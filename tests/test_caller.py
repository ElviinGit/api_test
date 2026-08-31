import calculate
from utils.my_decorator import log_test, take_screenshot_on_failure

@log_test
def test_calculate_sum_normal():
    result = calculate.calculate_sum(3, 5)
    assert result == 8, f"Expected 8 but got {result}"

@log_test
@take_screenshot_on_failure
def test_calculate_sum_with_exception():
    
    calculate.calculate_sum_with_exception(3, 5)


