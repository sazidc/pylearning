# paint area calculatuor
import math


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


testh = int(input("Height of wall: "))
testw = int(input("Width of wall: "))
coverage = 5
paint_calc(height=testh, width=testw, cover=coverage)
