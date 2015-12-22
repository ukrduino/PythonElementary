# Write a program that produces Fibonacci numbers and is based on generators.
# The user should input a number that limits the number of results.


def fibonacci_generator(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def fibonacci_numbers(limit):
    """
    Produces Fibonacci numbers and is based on generator
    >>> fibonacci_numbers(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    return [n for n in fibonacci_generator(limit)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
