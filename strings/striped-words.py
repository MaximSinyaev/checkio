#!/home/poligon/.local/bin/checkio --domain=py run striped-words

# Our robots are always working to improve their linguistic skills.
# For this mission, they research the latin alphabet and its applications.
# 
# The alphabet contains both vowel and consonant letters (yes, we divide the letters).
# Vowels --A E I O U Y
# Consonants --B C D F G H J K L M N P Q R S T V W X Z
# 
# You are given a block of text with different words.
# These words are separated by white-spaces and punctuation marks.
# Numbers are not considered words in this mission (a mix of letters and digits is not a word either).
# You should count the number of words (striped words) where the vowels with consonants are alternating,
# that is; words that you count cannot have two consecutive vowels or consonants.
# The words consisting of a single letter are not striped -- do not count those.
# Casing is not significant for this mission.
# 
# Input:A text as a string (unicode)
# 
# Output:A quantity of striped words as an integer.
# 
# Precondition:The text contains only ASCII symbols.
# 0 < len(text) < 105
# 
# 
# END_DESC

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
punctuation = ",.!?"


def checkio(text):
    count = 0
    flag = {'v': 0, 'c': 0}
    for sep in punctuation:
        text = text.replace(sep, " ")
    for word in text.split():
        flag['c'], flag['v'] = 0, 0
        if len(word) <= 1:
            continue
        for letter in word:
            if letter.upper() in VOWELS:
                flag['v'] += 1
                flag['c'] = 0
            elif letter.upper() in CONSONANTS:
                flag['c'] += 1
                flag['v'] = 0
            else:
                flag['c'], flag['v'] = 0, 0
                break
            if flag['c'] + flag['v'] > 1:
                break
        if abs(flag['v'] + flag['c']) == 1:
            # print(word)
            count += 1
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(checkio("To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?"))
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
