# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html


def bubble_sort(un_list):
    for passnum in range(len(un_list) - 1, 0, -1):
        for i in range(passnum):
            if un_list[i] > un_list[i + 1]:
                temp = un_list[i]
                un_list[i] = un_list[i + 1]
                un_list[i + 1] = temp


unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(unsorted_list)
print(unsorted_list)
