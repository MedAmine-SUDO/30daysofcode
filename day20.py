#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numer_of_swap = 0
for i in range(0, len(a)):
    for j in range(0, len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numer_of_swap += 1
    if numer_of_swap == 0:
        break
print("Array is sorted in {} swaps.".format(numer_of_swap))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))