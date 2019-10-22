def count_consecutive_summers(num):
    sum = 0
    sums = 1
    arif_sum = lambda n, a1, d: n * (a1 + (n - 1) * d) // 2
    for i in range(1, (num + 1) // 2):
        for j in range(1, (num + 1) // 2):
            sum = arif_sum((j + 1) // 2, i, 1)
            # print(sum)
            if sum == num:
                sums += 1
            elif sum > num:
                break
        # while (sum <= num):
        #     sum += i + k
        #     k += 1
        #     if sum == num:
        #         sums += 1
        # sum = 0
    print(sums)
    return sums

if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(4543532))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")