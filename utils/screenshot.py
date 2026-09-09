from datetime import datetime
from pathlib import Path

def take_screenshot(driver, test_name):
 
    Path("screenshots").mkdir(exist_ok=True)  # Create the screenshots directory if it exist
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = Path("screenshots") / f"{test_name}_{timestamp}.png"  
    try:
        driver.save_screenshot(screenshot_path)
    except Exception as e:
        print(f"Failed to take screenshot: {e}")
        return None
     
    return screenshot_path

