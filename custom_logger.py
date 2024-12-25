import logging
import os
from datetime import datetime

def setup_custom_logger(name):
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Create a custom logger
    logger = logging.getLogger(name)
    
    # Set the minimum logging level (e.g., DEBUG)
    logger.setLevel(logging.DEBUG)
    
    # Create a file handler that logs to a file with the current date as its name
    log_filename = os.path.join('logs', f'{datetime.now().strftime("%Y-%m-%d")}.log')
    fh = logging.FileHandler(log_filename)
    fh.setLevel(logging.DEBUG)
    
    # Create a formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    # Add the file handler to the logger
    logger.addHandler(fh)
    
    return logger
