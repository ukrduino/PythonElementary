# Write a program that computes the number of occurrences of each symbol in
# a string. The string is provided by the program.
import random
import string

rand_str = ''.join(random.choice(string.lowercase) for _ in range(100))


def string_sorter(string_to_sort):
    chars_dict = dict()
    for char in string_to_sort:
        if char in chars_dict.keys():
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    for char, number in chars_dict.items():
        print "char [" + char + "] - " + str(number)

print string
string_sorter(rand_str)
