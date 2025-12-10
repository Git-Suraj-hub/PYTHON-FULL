import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    def decorated(*args, **kwargs):
        func_name = func.__name__  # Get the function's name
        logging.info(f"Calling {func_name} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func_name} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a * b

# Call the function
my_function(a=3, b=4)
