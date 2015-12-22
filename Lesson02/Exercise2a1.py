# Write a bubble-sort function


def bubble_sort(un_list):
    """
    Bubble-sort function
    >>> unsorted_list = [54, 26, 93, 17, -77, 31, 44, 55, 200000]
    >>> bubble_sort(unsorted_list)
    >>> print unsorted_list
    [-77, 17, 26, 31, 44, 54, 55, 93, 200000]
    """
    for pass_number in range(len(un_list) - 1, 0, -1):
        for i in range(pass_number):
            if un_list[i] > un_list[i + 1]:
                un_list[i], un_list[i + 1] = un_list[i + 1], un_list[i]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
