#!/home/poligon/.local/bin/checkio --domain=py run seven-segment

# You have a device that uses aSeven-segment displayto display 2 digit numbers.However, some of the segments aren't working and can't be displayed.
# 
# You will be given information on the lit and broken segments.You won't know whether the broken segment is lit or not.You have to count and return the total number that the device may be displaying.
# 
# The input is a set of lit segments (the first argument) and broken segments (the second argument).
# 
# Uppercase letters represent the segments of the first out two digit number.Lowercase letters represent the segments of the second out two digit number.topmost: 'A(a)', top right: 'B(b)', bottom right: 'C(c)', bottommost: 'D(d)', bottom left: 'E(e)', top left: 'F(f)', middle: 'G(g)'
# 
# 
# 
# Input:Two arguments. The first one contains the lit segments as a set of letters representing segments. The second one contains the broken segments as a set of letters representing segments.
# 
# Output:The total number that the device may be displaying.
# 
# 
# 
# Precondition:
# all(re.match('[A-Ga-g]', s) for s in lit | broken)len(lit  &  broken) == 0
# 
# 
# END_DESC

nums = {
    1: {'b', 'c'},
    2: set(i for i in 'abged'),
    3: set(i for i in 'abgcd'),
    4: set(i for i in 'fgbc'),
    5: set(i for i in 'afgcd'),
    6: set(i for i in 'afgcde'),
    7: set(i for i in 'abc'),
    8: set(i for i in 'abcdefg'),
    9: set(i for i in 'abcdfg'),
    0: set(i for i in 'abcdef')
}

def combinations(broken, subs, dig, dig_vars):
    for i in broken:
        subs.add(i)
        combinations(broken - set(i), subs, dig, dig_vars)
        for i, sub in nums.items():
            if (broken | dig) == sub:
                dig_vars.add(i)

def seven_segment(lit_seg, broken_seg):
    first_dig = set()
    first_dig_br = set()
    first_dig_vars = set()
    second_dig = set()
    second_dig_br = set()
    second_dig_vars = set()
    for segment in lit_seg:
        if segment.isupper():
            first_dig.add(segment.lower())
        else:
            second_dig.add(segment)
    for i, seq in nums.items():
        if seq == first_dig:
            first_dig_vars.add(i)
        if seq == second_dig:
            second_dig_vars.add(i)
    for i in broken_seg:
        if i.isupper():
            first_dig_br.add(i.lower())
        else:
            second_dig_br.add(i)
    combinations(first_dig_br, set(), first_dig, first_dig_vars)
    combinations(second_dig_br, set(), second_dig, second_dig_vars)
    l1 = len(first_dig_vars)
    l2 = len(second_dig_vars)
    # sum = l2 if (0 in first_dig_vars) else 0
    sum = 0
    sum += l1 * l2
    return sum


if __name__ == '__main__':
    seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'})
    seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'})
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'}) == 4, '0, 8, 80'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')