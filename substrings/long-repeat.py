#!/home/poligon/.local/bin/checkio --domain=py run long-repeat

# There are four substring missionsthat were born all in one day and you shouldn’t need more than one day to solve them. All of these missions can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
# 
# This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one, which makes it the answer.
# 
# Input:String.Output:Int.
# 
# 
# 
# 
# END_DESC

def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """

    l = len(line)
    if l == 0:
        return 0
    words = list()
    k = i = 1
    max_l = 0
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            k += 1
        else:
            words.append(line[i - k: i])
            max_l = max(max_l, k)
            k = 1
    words.append(line[i - k: i])
    max_l = max(max_l, k) 
    return max_l

if __name__ == '__main__':
    print(long_repeat('aa'))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')