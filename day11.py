#!/bin/python3

import math
import os
import random
import re
import sys

def initialize_y(arr):
    y_coor = [0, 1, 2, 1, 0, 1, 2]
    x_coor = [x for x, y in arr]
    arr = [(x, y) for x, y in zip(x_coor, y_coor)]
    return arr

def incriment_x(arr, n):
    arr = [(x+n, y) for (x, y) in arr]
    return arr

def incriment_y(arr, n):
    arr = [(x, y+n) for (x, y) in arr]
    return arr

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglass_init= [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 1),
        (2, 0),
        (2, 1),
        (2, 2),
    ]

    sums = []

    for i in range(16):
        if i == 0:
            hourglass = hourglass_init
        elif i % 4 == 0 and i != 0:
            hourglass = initialize_y(hourglass)
            hourglass = incriment_x(hourglass, 1)
        else:
            hourglass = incriment_y(hourglass, 1)
            
        values = [arr[x][y] for x, y in hourglass]
        sums.append(sum(values))

print(max(sums))
            

