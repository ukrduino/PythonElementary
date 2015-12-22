# Write a decorator class profile that will compute the functions execution
# time, number of calls, and call the hierarchy of functions
# decorated with profile
import cProfile
import pstats
import sys

from Lesson02.Exercise2_1 import factorial_loop


class Profiled(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        res = self.func(*args, **kwargs)
        profiler.disable()
        ps = pstats.Stats(profiler, stream=sys.stdout)
        ps.print_stats()
        return res


@Profiled
def factorial_l(n):
    return factorial_loop(n)


if __name__ == "__main__":
    result1 = factorial_l(50000)
    print result1

