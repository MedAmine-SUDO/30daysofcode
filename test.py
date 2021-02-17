hourglass= [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 1),
        (2, 0),
        (2, 1),
        (2, 2),
    ]

def initialize_y(arr):
    y_coor = [0, 1, 2, 1, 0, 1, 2]
    x_coor = [x for x, y in arr]
    arr = [(x, y) for x, y in zip(x_coor, y_coor)]
    return arr

for i in range(16):
    print(hourglass)
    if i % 4 == 0 and i != 0:
        hourglass = initialize_y(hourglass)
        hourglass = [(x+1, y) for x, y in hourglass]
    else:
        hourglass = [(x, y+1) for x, y in hourglass]
