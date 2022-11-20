#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Nov 4
# The code prints numbers in range 1000-2000 on a new line every 5 numbers.


def main():
    # I defined the integers in the range as int for readability.
    # +1 is due to how range is in python.
    for int in range(1000, 2000 + 1, 1):
        # for every 5 numbers a new line will be created.
        if int % 5 == 0:
            print(int)
            print()
            continue
        # I used the parameter "end= " so that print does not start a new line.
        print(int, end=" ")


if __name__ == "__main__":
    main()
