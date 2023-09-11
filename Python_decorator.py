import time
"""
def my_decorator(func):
    def wrapper():
        print("Before callling the function")
        func()
        print("After calling the function")
    return wrapper


@my_decorator
def greet():
    print("Hello how are you")


greet()
"""

# repeating the function

"""
def repeating_function(number):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("I will execute in 2nd no.")
            for _ in range(number):
                func(*args, **kwargs)
        return wrapper
    print("I will execute first")
    return decorator


@repeating_function(3)
def greet(name):
    print(f"Hello {name}")


greet("Ehtsham")
"""
# Decorator using time


def start_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function is executing in {end_time-start_time} seconds")
        return result
    return wrapper


@start_time_decorator
def slow_function():
    time.sleep(2)
    print("Slow function")


slow_function()
