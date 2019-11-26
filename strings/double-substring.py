#!/home/poligon/.local/bin/checkio --domain=py run double-substring

# There are four substring missionsthat were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This is the third mission of the series, and it’s the only one where you have to return not a substring but a substring length. You need to find a substring that repeats more than once in a given string. This reiteration shouldn't have overlaps. For example, in a string "abcab" the longest substring that repeats more than once is "ab", so the answer should be 2 (length of "ab")
# 
# Input:String.Output:Int.
# 
# 
# 
# 
# END_DESC

def double_substring(line):
    """
        length of the longest substring that non-overlapping repeats more than once.
    """
    l = len(line)
    subs = dict()
    subs_l = []
    for l_sub in range(l // 2, 0, -1):
        subs_l.extend([line[i:i + l_sub] for i in range(0, l - l_sub)])
    #subs_l = set(subs_l)
    l = 0
    for i in subs_l:
        if line.count(i) > 1:
            print(len(i))
            return len(i)
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    assert double_substring('arefhjaref') == 4
    assert double_substring('aa') == 1
    print('"Run" is good. How is "Check"?')