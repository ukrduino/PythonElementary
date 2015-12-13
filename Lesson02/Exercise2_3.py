# Write a function adding two numbers in the following manner: add(1)(2) == 3


def add(n):
    return lambda x: n + x

# print add(10)(5)
#
# print add("Hellow")(" world")
#
# print add([77])([10])
