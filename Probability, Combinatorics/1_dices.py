# Probably Dice

'''
Typically, when using multiple dice, you simply roll them and sum up all the result.
To get started with your investigation of dice probability, write a function that takes the number
of dice, the number of sides per die and a target number and returns the probability of getting
a total roll of exactly the target value.
The result should be given with four digits precision as ±0.0001.
'''

def combinations(k, n):
    result = 1
    if k == 0:
        return 1
    for i in range(k, n + 1):
        result *= k
    for i in range(1, n - k):
        result /= i
    return result

def probability(dice_number, sides, target):
    distribution = list()
    if not((target >= dice_number) & (target <= dice_number * sides)):
        return 0.0
    c = combinations(1, dice_number)  # combinations of 1 point in number of dices ([1 2], [2,1])
    all_comb = sides ** dice_number
    all_comb_inv = 1 / all_comb # inverse value, for faster working program, because multiply is faster
    average = (dice_number * sides + dice_number) // 2
    print(">>", average, all_comb, c)
    for i in range(dice_number, average + 1):
        distribution.append(round(c * (i - dice_number + 1) * all_comb_inv, 4))
    if len(distribution) % 2 == 0:
        distribution.extend(distribution[::-1])
    else:
        distribution.extend(distribution[:-2:-1])
    print(distribution[target - dice_number])
    print(distribution)
    return distribution[target - dice_number]


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    print("my", probability(3, 6, 7))
    print("-"*20)

    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"