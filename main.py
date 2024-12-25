from custom_logger import setup_custom_logger

# Set up the logger
logger = setup_custom_logger('MyLogger')

# Example usage of the logger
def some_function():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

# Call the function to see the logging in action
if __name__ == "__main__":
    some_function()
