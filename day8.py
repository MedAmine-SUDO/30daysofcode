#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    phone_book = {}

    while n != 0:
        arr = list(input().rstrip().split())
        phone_book[arr[0]] = arr[1]

        n -= 1

    list_to_look_for = []
    while True:
        try:
            nom = list(input().rstrip().split())
            if not nom:
                break
            list_to_look_for.append(nom[0])
        except (EOFError):
            break
        


    for nom in list_to_look_for:
        if nom in phone_book.keys():
            print(nom+'='+phone_book[nom])
        else:
            print("Not found")