#!/bin/python3

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

X_UPPER_BOUNDARY = 0
Y_UPPER_BOUNDARY = 0


def calculate_diff(element, neighbor):
    diff = 0 if element - neighbor < 0 else element - neighbor
    return diff


def calculate_element_area(A, x, y):
    current_element = A[y][x]

    value_left = 0 if x - 1 < 0 else A[y][x - 1]
    value_right = 0 if x + 1 > X_UPPER_BOUNDARY else A[y][x + 1]
    value_above = 0 if y - 1 < 0 else A[y - 1][x]
    value_below = 0 if y + 1 > Y_UPPER_BOUNDARY else A[y + 1][x]

    diff_left = calculate_diff(current_element, value_left)
    diff_right = calculate_diff(current_element, value_right)
    diff_above = calculate_diff(current_element, value_above)
    diff_below = calculate_diff(current_element, value_below)

    return diff_left + diff_right + diff_below + diff_above + 2


def surfaceArea(A):
    # Write your code here
    surface_area = 0
    for row, val in enumerate(A):
        for col, val in enumerate(val):
            print("x: {} / y: {}".format(col, row))
            if A[row][col] == 0:
                surface_area += 0
            else:
                surface_area += calculate_element_area(A, col, row)

    return surface_area


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])
    Y_UPPER_BOUNDARY = H - 1

    W = int(first_multiple_input[1])
    X_UPPER_BOUNDARY = W - 1

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)
    print(result)
