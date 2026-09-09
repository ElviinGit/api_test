from utils.screenshot import take_screenshot
from utils.logger import my_logger
from functools import wraps


def screenshot_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        my_logger.info("Function starting decorating")
        my_logger.info(f"args: {args}")
        my_logger.info(f"kwargs: {kwargs}")

        try:
            result = func(*args, **kwargs)

        except Exception as e:
            driver = kwargs.get("driver")
            test_name = func.__name__

            # Try to find driver in args
            if driver is None:
                for item in args:
                    if hasattr(item, "save_screenshot"):
                        driver = item
                        break

            # Check whether driver was found
            if driver is None:
                my_logger.error(
                    f"Driver not found for {func.__name__}: {e}"
                )
                raise

            # Driver was found → take screenshot
            screenshot_path = take_screenshot(driver, test_name)

            if screenshot_path:
                my_logger.error(
                    f"An error occurred in {func.__name__}. "
                    f"Screenshot saved at: {screenshot_path}"
                )
            else:
                my_logger.error(
                    f"An error occurred in {func.__name__}. "
                    f"Failed to take screenshot."
                )

            # Preserve original test exception
            raise

        my_logger.info("Function finished decorating")
        return result

    return inner