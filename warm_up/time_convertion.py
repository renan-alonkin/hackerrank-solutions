#!/bin/python3


def timeConversion(s):
    hour_as_list = s.split(":")
    hour = int(hour_as_list[0])
    minutes = int(hour_as_list[1])
    seconds = int((hour_as_list[2][:2]))
    am_or_pm = hour_as_list[2][-2:].lower()

    if am_or_pm == "am":
        hour = (hour + 12) % (12)
    if am_or_pm == "pm":
        hour = (hour % 12) + 12
    new_s = "{:02d}:{:02d}:{:02d}".format(hour, minutes, seconds)

    return new_s
    # Write your code here


if __name__ == "__main__":

    s = input()

    result = timeConversion(s)
    print(result)
