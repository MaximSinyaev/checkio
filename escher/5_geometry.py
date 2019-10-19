# Wild Dogs
'''
As input you’ll be given the coordinates of the dogs. Your task is to find the distance to the nearest point from which
you can kill the maximum number of animals with one shot (any number of dogs on the same line can be killed with one shot).
Your starting position is the point (0, 0).

If the calculated distance is an integer, return it as int, otherwise round it to 2 decimal places.
Don't worry about the situation when a few dogs on the line is behind your back (dog dog you dog) - there no such situation in the tests.
'''


def wild_dogs(coords):
    l = len(coords)
    lines = list()  # list of k and b parametrs from equation y = k*x + b
    dots = list()
    for p1 in range(l):
        # first point of equation (x1, y1)
        for p2 in range(p1 + 1, l):
            # second point of equation (x2, y2)
            if (coords[p1][0] - coords[p2][0]) == 0:
                continue
            k = (coords[p1][1] - coords[p2][1]) / (coords[p1][0] - coords[p2][0])
            b = (coords[p1][0] * coords[p2][1] - coords[p2][0] * coords[p1][1]) /\
                (coords[p1][0] - coords[p2][0])
            if not((k, b) in lines):
                lines.append((k, b))
                dots.append(1)
            else:
                dots[lines.index((k, b))] += 1
    max_val = max(dots)    # lines with most dots for same number of dots
    max_i = [i for i, el in enumerate(dots) if max_val == el]   # list of indexes with max value
    r = 200.0   # max distance
    for i in max_i:
        # search for the shortest distance
        r = min(abs(lines[i][1] / (lines[i][0] ** 2 + 1) ** (1 / 2)), r)
    if r - int(r) == 0.0:
        r = int(r)
    else:
        r = round(r, 2)
    return abs(r)

if __name__ == '__main__':
    print("Example:")
    wild_dogs([[10, 23], [4, 5], [7, 14], [10, 110]])
    print(wild_dogs([(7, 122), (8, 139), (9, 156),
                     (10, 173), (11, 190), (-100, 1)]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156),
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
