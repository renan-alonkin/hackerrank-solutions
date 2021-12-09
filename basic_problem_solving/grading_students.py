#!/bin/python3


def gradingStudents(grades):
    # Write your code here
    results = []
    for grade in grades:
        diff_to_next_multiple_of_5 = 5 - (grade % 5)

        rounded_grade = grade + diff_to_next_multiple_of_5
        minor_than_40 = rounded_grade < 40
        bigger_than_3 = diff_to_next_multiple_of_5 >= 3

        results.append(grade) if (bigger_than_3 or minor_than_40) else results.append(
            rounded_grade
        )

    return results


if __name__ == "__main__":
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print("\n".join(map(str, result)))
