#!/bin/python3

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def calculate_factorial(n):
    if n > 1:
        return n * calculate_factorial(n - 1)
    else:
        return 1


def extraLongFactorials(n):
    # Write your code here
    print(calculate_factorial(n))


if __name__ == "__main__":
    n = int(input().strip())

    extraLongFactorials(n)
