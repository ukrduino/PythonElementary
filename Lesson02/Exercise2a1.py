# Write a bubble-sort function


def bubble_sort(un_list):
    for pass_number in range(len(un_list) - 1, 0, -1):
        print "pass #" + str(pass_number)
        for i in range(pass_number):
            print "pair [" + str(i) + ":" + str(i + 1) + "]"
            print un_list[i]
            print un_list[i + 1]

            if un_list[i] > un_list[i + 1]:
                print "change"
                un_list[i], un_list[i + 1] = un_list[i + 1], un_list[i]
                print un_list[i]
                print un_list[i + 1]


unsorted_list = [54, 26, 93, 17, -77, 31, 44, 55, 200000]
bubble_sort(unsorted_list)
print(unsorted_list)
