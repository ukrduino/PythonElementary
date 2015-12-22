# Write a recursive function that computes factorial

# In mathematics, the factorial of a non-negative integer n, denoted by n!,
# is the product of all positive integers less than or equal to n. For example,
# 5! = 5  *  4  *  3  *  2  *  1 = 120.


def factorial_rec(n):
    """
    Computing factorial using recursion
    >>> print factorial_rec(10)
    3628800
    """

    if n < 2:
        return 1
    else:
        return n * factorial_rec(n - 1)


def factorial_loop(n):
    """
    Computing factorial using loop
    >>> print factorial_loop(10)
    3628800
    """
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


if __name__ == "__main__":
    import doctest
    doctest.testmod()
