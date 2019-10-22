# The secret room

'''
As input your function will receive an integer - the total number of
doors in the current room. You will need to sort the door numbers in the order
in which these numbers, expressed in words, go in the alphabetical order.
And then return the position number of the last door (the door with the highest number).
The count starts from the 1st position (not from the 0th).
The maximum number of doors is 1000. The numbers after 100 are written in the
format like - 'one hundred twenty nine'.

Input: the door number.

Output: the 'right' door number.
'''

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"


def num2words(number):
    str = ""
    pow = 0
    while number >= 10 ** (pow + 1):
        pow += 1
    max_val = 10 ** pow
    while (pow > -1):
        if number == 1000:
            return "one thousand"
        if pow == 2:
            str += FIRST_TEN[number // max_val - 1] + ' ' + HUNDRED
            if (number % 10) != 0 or number % 100 != 0:
                str += ' '
        elif pow == 1 and number // 10 != 0:
            if (number < 20):
                str += SECOND_TEN[number % 10]
                pow = 0
            else:
                str += OTHER_TENS[number // max_val - 2]
                if (number % 10) != 0:
                    str += ' '
        elif pow == 0 and number != 0:
            str += FIRST_TEN[number - 1]
        number %= max_val
        max_val //= 10
        pow -= 1
    return str


def secret_room(num):
    words = list()
    for i in range(1, num + 1):
        words.append((i, num2words(i)))
    words.sort(key=lambda x: x[1])
    return words.index((num, num2words(num)))
    # print(words)


secret_room(5) == 1, #five, four, one, three, two

secret_room(3) == 2, #one, three, two

secret_room(1000) == 551

