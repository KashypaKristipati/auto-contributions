################################################################################
# Learning Objective:
# This tutorial will teach you how to build a personalized logging decorator
# in Python to automatically track the execution of your functions.
# Decorators are a powerful Python feature that allow you to modify or enhance
# functions without altering their original code. We'll use them to add logging
# to any function with minimal effort.
################################################################################

# Import the 'wraps' decorator from 'functools'.
# The 'wraps' decorator is crucial for preserving the original function's metadata
# (like its name and docstring) when using our custom decorator.
# Without it, the decorated function would appear to have the name and docstring
# of the decorator itself, which can be confusing.
from functools import wraps

# Define our custom logging decorator function.
# A decorator is essentially a function that takes another function as an argument,
# adds some functionality, and then returns the modified function.
def log_function_execution(func):
    # Use @wraps to preserve the original function's metadata.
    # This is a best practice when creating decorators.
    @wraps(func)
    # Define the wrapper function. This is the function that will actually
    # be executed when the decorated function is called.
    def wrapper(*args, **kwargs):
        # --- Logging Before Function Execution ---
        # We're logging here BEFORE the original function 'func' is called.
        # This allows us to see what's happening just as the function starts.

        # Log the name of the function being called.
        # '__name__' is a special attribute of a function that holds its name.
        print(f"INFO: Entering function '{func.__name__}'")

        # Log the arguments passed to the function.
        # '*args' captures all positional arguments as a tuple.
        # '**kwargs' captures all keyword arguments as a dictionary.
        # This helps in understanding what data the function received.
        print(f"INFO: Arguments: args={args}, kwargs={kwargs}")

        # --- Execute the Original Function ---
        # This is the core of the decorator. We call the original function 'func'
        # and pass it all the arguments it received.
        # We store the result so we can return it later and also log it.
        try:
            result = func(*args, **kwargs)

            # --- Logging After Function Execution (Success) ---
            # If the function executes without raising an exception, we log
            # its successful completion and its return value.
            print(f"INFO: Exiting function '{func.__name__}' successfully.")
            # Log the return value. This is very useful for debugging and understanding
            # what a function produced.
            print(f"INFO: Return value: {result}")

            # Return the original function's result. This is essential for the
            # decorated function to behave as expected.
            return result
        except Exception as e:
            # --- Logging After Function Execution (Error) ---
            # If the function raises an exception, we catch it and log the error.
            # This is crucial for identifying and fixing bugs.
            print(f"ERROR: Exception in function '{func.__name__}': {e}")
            # Re-raise the exception. It's important to re-raise the exception
            # so that calling code can handle it appropriately. If we didn't
            # re-raise, the exception would be silently swallowed, which is bad.
            raise

    # The decorator returns the 'wrapper' function.
    # This 'wrapper' function replaces the original function 'func'
    # wherever the decorator is applied.
    return wrapper

# --- Example Usage ---

# Apply the decorator to a function.
# The '@log_function_execution' syntax is syntactic sugar for:
# my_function = log_function_execution(my_function)
@log_function_execution
def add_numbers(a, b):
    """
    This function adds two numbers.
    """
    print(f"DEBUG: Inside add_numbers. Calculating {a} + {b}.")
    return a + b

@log_function_execution
def greet(name, greeting="Hello"):
    """
    This function greets a person.
    """
    print(f"DEBUG: Inside greet. Constructing greeting for {name}.")
    return f"{greeting}, {name}!"

@log_function_execution
def divide_numbers(x, y):
    """
    This function divides two numbers. It might raise a ZeroDivisionError.
    """
    print(f"DEBUG: Inside divide_numbers. Calculating {x} / {y}.")
    return x / y

# Call the decorated functions and observe the logging output.
print("--- Calling add_numbers ---")
sum_result = add_numbers(5, 3)
print(f"Actual result of add_numbers: {sum_result}\n")

print("--- Calling greet ---")
greeting_message = greet("Alice")
print(f"Actual result of greet: {greeting_message}\n")

print("--- Calling greet with keyword argument ---")
custom_greeting = greet("Bob", greeting="Hi")
print(f"Actual result of greet: {custom_greeting}\n")

print("--- Calling divide_numbers (successful case) ---")
division_result = divide_numbers(10, 2)
print(f"Actual result of divide_numbers: {division_result}\n")

print("--- Calling divide_numbers (error case) ---")
try:
    error_result = divide_numbers(10, 0)
    print(f"Actual result of divide_numbers (error case): {error_result}\n")
except ZeroDivisionError:
    print("Successfully caught ZeroDivisionError as expected.\n")

# Demonstrate that the original function's metadata is preserved.
print(f"Name of decorated add_numbers function: {add_numbers.__name__}")
print(f"Docstring of decorated add_numbers function: {add_numbers.__doc__}")
print("\n--- End of Tutorial ---")