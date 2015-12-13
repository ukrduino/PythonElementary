def string_sorter(string_to_sort):
    chars_dict = dict()
    for char in string_to_sort:
        if char in chars_dict.keys():
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    for char, number in chars_dict.items():
        print "char [" + char + "] - " + str(number)
    return chars_dict
