#!/usr/bin/python3

size = int(input("Enter the size of the pattern: "))
row_count = size

while row_count > 0:
    for i in range(size):
        print("* ", end="")
    row_count -= 1
    print()