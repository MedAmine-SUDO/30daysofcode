import math
import os
import random
import re
import sys

def longestSubarray(arr):
    # Write your code here
    
    l = []
    if len(arr) == 1:
        return 1
    else:
        for i in range(len(arr)):
            longest = 0

            if i == (len(arr) - 2):
                longest = 1
                l.append(longest)
            for j in range(i+1, len(arr)):
                if abs(arr[i] - arr[j]) <= 1:
                    if (abs(i - j) == 1):
                        longest += 2
                    if abs(i - j) > 1:
                        longest += 1
                    l.append(longest)
                else:
                    break
            
            
        return max(l)

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    print(result)

