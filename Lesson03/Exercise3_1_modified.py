def string_sorter(string_to_sort):
    chars_dict = dict()
    for char in string_to_sort:
        if char in chars_dict.keys():
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict
