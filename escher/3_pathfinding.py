# Compass, Map and Spyglass
'''
    Your task is to count the sum of the number of steps required to pick up all 3 items - ('C' - compass), ('M' - map), ('S' - spyglass) from your starting position.
So the result will be the sum of distance from Y to C, from Y to M and from Y to S (not Y-C-M-S).

   Note that you can walk in 8 directions - left, right, up, down and sideways (on the diagonal in any direction).
Your starting position is 'Y'. 
'''

def navigation(seaside):
    '''
    seaside - seaside map which represented by matrix has only 4 type of objects
    Y, M, C, S.
    '''
    coords = dict(zip(('Y', 'M', 'C', 'S'), zip([0 for _ in range(4)], [0 for _ in range(4)])))
    m = len(seaside)
    n = len(seaside[0])
    for i in range(m):
        for j in range(n):
            if (seaside[i][j] == 'Y'):
                coords['Y'] = i, j
            elif (seaside[i][j] == 'C'):
                coords['C'] = i, j
            elif (seaside[i][j] == 'M'):
                coords['M'] = i, j
            elif (seaside[i][j] == 'S'):
                coords['S'] = i, j
    y_c = max(abs(coords['Y'][0] - coords['C'][0]), abs(coords['Y'][1] - coords['C'][1]))
    y_m = max(abs(coords['Y'][0] - coords['M'][0]), abs(coords['Y'][1] - coords['M'][1]))
    y_s = max(abs(coords['Y'][0] - coords['S'][0]), abs(coords['Y'][1] - coords['S'][1]))
    return y_c + y_m + y_s

if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
