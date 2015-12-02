# Write a program that produces Fibonacci numbers and is based on generators.
# The user should input a number that limits the number of results.


def fibonacci(fibonachi_number):
    a, b = 0, 1
    while a < fibonachi_number:
        yield a
        a, b = b, a + b

for n in fibonacci(100):
    print n
