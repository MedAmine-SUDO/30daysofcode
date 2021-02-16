#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    arr = list(input().rstrip().split())

    print(' '.join(arr[::-1]))