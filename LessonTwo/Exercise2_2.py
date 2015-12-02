# Write a function computing the average from arbitrary numbers of an argument.
# For example: avg(4, 5, 2, 3)


def avg(*args):
    # Filtering input from non numeric types
    list_of_numbers = [x for x in args if x.__class__ in [int, float, long]]
    # The float() is necessary to force Python to do a floating-point division.
    return sum(list_of_numbers)/float(len(list_of_numbers))

# print avg(5, 11, 5.54576984576954769856798578, 11, "kk")
# print avg(4, 5, 2, 3)
