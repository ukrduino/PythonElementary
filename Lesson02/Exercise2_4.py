# Write a decorator that computes the execution time of the decorated function
import time

from Lesson02.Exercise2_1 import factorial_loop
from Lesson02.Exercise2_1 import factorial_rec


def wrapped_with_timer(func):
    """
    Computes the execution time of the decorated function
    """
    def wrapper(*args, **kwargs):
        time_of_start = time.clock()
        wrapped_function = func(*args, **kwargs)
        print func.__name__, "calculated in ", time.clock() - time_of_start, \
            "seconds"
        return wrapped_function
    return wrapper


@wrapped_with_timer
def factorial_r(n):
    return factorial_rec(n)


@wrapped_with_timer
def factorial_l(n):
    return factorial_loop(n)


if __name__ == "__main__":
    factorial_r(500)
    factorial_l(500)
