import math


def paint_calc(height, width, cover):
    no_of_cans = math.ceil((height * width)/cover)  # dont use round,if output is 18.2 it will round to 18 but we need 19 cans of paint so ceil function to be used
    print(no_of_cans)


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)  #passed as keyword arguments instead of positional arg