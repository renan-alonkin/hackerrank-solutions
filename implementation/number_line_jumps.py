#!/bin/python3


def kangaroo(x1, v1, x2, v2):
    # Write your code here

    # Equation of intersection:
    # x1 + t*v1 = x2 + t*v2
    # x1 - x2 = t*v2 - t*v1
    # x1 - x2 = t*(v2 - v1)
    # (x1 - x2)/(v2 - v1) = t
    # Time is an integer, so, if they meet, the module
    # needs to be 0, if module > 0 they don't meet

    if (
        ((x1 > x2) and (v1 > v2))  # x1 is ahead
        or ((x2 > x1) and (v2 > v1))  # x2 is ahead
        or ((x1 == x2) and (v1 != v2))  # are equal but diff speed
        or ((x1 != x2) and (v1 == v2))  # Eq speed, diff starts
    ):
        return "NO"
    else:
        if (x1 - x2) % (v2 - v1) == 0:
            return "YES"
    return "NO"


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + "\n")
