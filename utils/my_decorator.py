import time
from functools import wraps
from .my_logger import logger
from pathlib import Path
from datetime import datetime

ss_dir = Path("screenshots")
ss_dir.mkdir(exist_ok=True)


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
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{func.__name__}_failure_{timestamp}.png"
            screenshot_path = ss_dir / f"{filename}"
            # Simulate taking a screenshot (replace with actual screenshot logic)
            with open(screenshot_path, "wb") as f:
                f.write(b"Simulated screenshot content")
            logger.error(f"Screenshot taken: {screenshot_path}")
            raise 
        
    return inner

