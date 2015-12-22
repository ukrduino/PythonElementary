# Write a function computing the average from arbitrary numbers of an argument.
# For example: avg(4, 5, 2, 3)


def avg(*args):
    """
    Computing the average from arbitrary numbers of an argument
    >>> print avg(5, 11, 5.54, 11, "kk")
    8.135
    >>> print avg(4, 5, 2, 3)
    3.5
    """
    # Filtering input from non numeric types
    list_of_numbers = [x for x in args if x.__class__ in [int, float, long]]
    # The float() is necessary to force Python to do a floating-point division.
    return sum(list_of_numbers)/float(len(list_of_numbers))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
