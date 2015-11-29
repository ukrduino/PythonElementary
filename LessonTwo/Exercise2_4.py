# Write a decorator that computes the execution time of the decorated function
import time
from LessonTwo.Exercise2_1 import factorial_rec
from LessonTwo.Exercise2_1 import factorial_loop


def wrapped_with_timer(func):
    def wrapper(*args, **kwargs):
        time_of_start = time.clock()
        wrapped_function = func(*args, **kwargs)
        print func.__name__, "calculated in ", time.clock() - time_of_start, \
            "seconds"
        return wrapped_function
    return wrapper


@wrapped_with_timer
def factorial_r(n):
    return factorial_rec(n)\

@wrapped_with_timer
def factorial_l(n):
    return factorial_loop(n)

# factorial_r(500)
# factorial_l(500)
