#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary_n = format(n, 'b')
    groups = [len(x) for x in binary_n.split('0')]
    print(max(groups))
 