# Write a program that generates and draws a simple labyrinth in ASCII mode.
# The labyrinth should consist of 6 different tiles (3x3 symbols) represented
# as string as follows

NO = '###' \
     '###' \
     '###'   # No path

LR = '###' \
     '   ' \
     '###'   # Path from left to right

LT = '# #' \
     '  #' \
     '###'   # Path from left to top

BR = '###' \
     '#  ' \
     '# #'   # Path from bottom to right

LB = '###' \
     '  #' \
     '# #'   # Path from left to bottom

TR = '# #' \
     '#  ' \
     '###'   # Path from top to right


def render(two_dem_array):
    for array_of_tiles in two_dem_array:
        print_string = ""
        for tile in array_of_tiles:
            print_string = print_string + tile[:3]
        print print_string
        print_string = ""
        for tile in array_of_tiles:
            print_string = print_string + tile[3:6]
        print print_string
        print_string = ""
        for tile in array_of_tiles:
            print_string = print_string + tile[6:]
        print print_string


render([
        [NO, BR, LR, LB, NO],
        [LR, LT, NO, TR, LR]
        ])
