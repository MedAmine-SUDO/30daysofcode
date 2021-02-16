#!/bin/python3

if __name__ == '__main__':
    t = int(input())
    words = []

    while t != 0:
        word = input()
        words.append(word)

        t -= 1

    for word in words:
        odd_chars = [x for i, x in enumerate(word) if i % 2 != 0]
        even_chars = [x for i, x in enumerate(word) if i % 2 == 0]

        print(''.join(even_chars) + ' ' + ''.join(odd_chars))
        

   