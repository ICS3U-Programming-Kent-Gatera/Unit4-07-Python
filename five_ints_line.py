#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Nov 4
# The code prints numbers in range 1000-2000 on a new line every 5 numbers.


def main():
    for int in range(1000, 2000, 1):
        if int % 5 == 0:
            print(int)
            print()
            continue
        print(int, end=" ")


if __name__ == "__main__":
    main()
