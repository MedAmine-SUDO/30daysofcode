if __name__ == '__main__':

    returned = list(map(int, input().strip().split(' ')))
    expected = list(map(int, input().strip().split(' ')))

    fine = 0

    if returned[2] > expected[2]:
        fine = 10000
    elif returned[2] == expected[2]:
        if returned[1] > expected[1]:
            fine = 500 * (returned[1]-expected[1])
        elif returned[0] > expected[0]:
            fine = 15 * (returned[0]-expected[0])
    print(fine)
        