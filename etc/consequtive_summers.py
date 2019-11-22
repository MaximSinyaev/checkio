def count_consecutive_summers(num):
    sums = 1
    arif_sum = lambda n, a1: n * (2 * a1 + (n - 1)) // 2
    for i in range(1, int((num * 2) ** 0.5) + 1):
        av = num // i
        for j in range(av - 2, av + 1):
            sum = arif_sum(j, i)
            if (j == (av - 2)) and sum > num:
                j = (i + av) // 2
                for k in range(j, 1, -2):
                    sum = arif_sum(k, i)
                    # print(sum)
                    if sum == num:
                        sums += 1
                        break
                    elif sum < num:
                        if (arif_sum(k + 1, i) == num):
                            sums += 1
                        break
                break
            if sum == num:
                sums +=1
                break
            elif sum > num:
                break
    return sums

if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(int(input())))
    print("-" * 25)
    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")