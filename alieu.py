def unwrap_function(func):
    """Unwraps a decorated function to get the original function."""
    while hasattr(func, '__wrapped__'):
        func = func.__wrapped__
    return func

# Example usage with a simple decorator:
def my_decorator(f):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = f(*args, **kwargs)
        print("After the function call")
        return result
    wrapper.__wrapped__ = f
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Get the original function
original_func = unwrap_function(say_hello)
print(original_func)  # Output: <function say_hello at 0x...>
