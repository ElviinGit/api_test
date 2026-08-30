import logging
from pathlib import Path
def my_logger():
    """This function sets up a logger for the automation project. It creates a log directory if it doesn't exist, configures the logger to log messages to both a file and the console, and sets the logging level to DEBUG."""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger("automation")
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)  # Set the logger level to DEBUG

    file_logger = logging.FileHandler(log_dir / "test_automation.log")
    console_logger = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_logger.setFormatter(formatter)
    console_logger.setFormatter(formatter)  

    if not logger.hasHandlers():
        logger.addHandler(file_logger)
        logger.addHandler(console_logger)  

    return logger 

logger = my_logger()