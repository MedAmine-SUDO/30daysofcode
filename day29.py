#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        
        s = set(range(1, n+1))
        final_result = 0
        for i in range(1, len(s)):
            for j in range(i+1, len(s)+1):
                bit_wise = i & j
                if bit_wise > final_result and bit_wise < k:
                    final_result = bit_wise

        print(final_result)
        
        #This is the optimized solution in term of time complexity
        print(k-1 if ((k-1) | k) <= n else k-2)