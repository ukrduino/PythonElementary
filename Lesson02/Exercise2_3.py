# Write a function adding two numbers in the following manner: add(1)(2) == 3


def add(n):
    """
    >>> print add(10)(5)
    15
    >>> print add("Hellow ")("world")
    Hellow world
    >>> print add([77])([10])
    [77, 10]
    """
    return lambda x: n + x


if __name__ == "__main__":
    import doctest
    doctest.testmod()

