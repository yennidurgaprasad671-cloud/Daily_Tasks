"""14. Performance Tracker (Decorators)
A software team wants to track how long functions take to execute. Create a decorator
that measures and prints the execution time of a function."""
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


# Example usage
@timer
def slow_function():
    time.sleep(2)


slow_function()
