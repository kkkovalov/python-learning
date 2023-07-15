def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper

@uppercase_decorator
def say_hi():
    """
    Function returns 'Hi there!' message in addition to its decorators
    """
    return 'Hi there!'

print(say_hi())


import functools
# Universal decorators
def a_passing_argument(function_to_decorate):
    @functools.wraps(function_to_decorate)
    def wrapper(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return wrapper

@a_passing_argument
def function_no_arg():
    print("Inside func, no args")
    
    
function_no_arg()

import time

def timer(function_to_decorate):
    @functools.wraps(function_to_decorate)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function_to_decorate(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        print(f"∆t = {dt}")
        return result
    return wrapper

def fibonacci(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError(f"{n} is not a positive integer")
    
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
@timer
def global_fib(n):
    return fibonacci(n)
    
print(global_fib(8))