# The Stone Wall

'''
    As input you'll get a multiline string consists of '0' and '#' - a view of a stone wall from above.
The '#' will show the stone part of the wall and the '0' will show the empty part.
The relative location of you and the wall is as follows: you look at the array from the bottom of it.

    Your task is to find the index of the place where the wall is the narrowest (as shown at the picture below).
The width of the wall is the height of the columns of the array (multiline string).
If there are several such places, return the index of leftmost. Index starts from 0. 
'''

def stone_wall(wall):
    '''
    wall - 2D matrix with 2 types of chars '0' and '#' (also "\n") that represents wall from above
    '''
    wall = wall[1:] if wall[0] == "\n" else wall
    l = len(wall)
    lines = 0
    for i in wall[1:]:
        if i == "\n":
            lines += 1
    cols = (l - lines) // lines
    min = lines
    min_i = 0
    for i in range(cols):
        temp = sum([1 for i in wall[i: l - 1: cols + 1] if i == '#'])
        if temp < min:
            min = temp
            min_i = i
    return min_i

if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##0
###
###
###
'''))

    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0
