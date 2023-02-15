import math


def calc_entropy():
    p1 = float(input()) / float(input())
    p2 = 1 - p1
    if p1 == 0:
        return "{:.2f}".format(-p2 * math.log2(p2))
    elif p2 == 0:
        return "{:.2f}".format(-p1 * math.log2(p1))
    else:
        return "{:.2f}".format(-p1 * math.log2(p1) - p2 * math.log2(p2))
