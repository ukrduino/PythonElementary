# Write a recursive function that computes factorial

# In mathematics, the factorial of a non-negative integer n, denoted by n!,
# is the product of all positive integers less than or equal to n. For example,
# 5! = 5  *  4  *  3  *  2  *  1 = 120.


def factorial_rec(n):
    if n < 2:
        return 1
    else:
        return n * factorial_rec(n - 1)


def factorial_loop(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


# print factorial_rec(100)
# print factorial_loop(100)
#
# print str(factorial_rec(100) == factorial_loop(100))