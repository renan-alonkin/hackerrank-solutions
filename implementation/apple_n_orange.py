#!/bin/python3


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apples_inside_border = 0
    for apple_d in apples:
        calc_apple_p = a + apple_d
        if calc_apple_p >= s and calc_apple_p <= t:
            apples_inside_border += 1

    oranges_inside_border = 0
    for orange_d in oranges:
        calc_orange_p = b + orange_d
        if calc_orange_p >= s and calc_orange_p <= t:
            oranges_inside_border += 1

    print(apples_inside_border)
    print(oranges_inside_border)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
