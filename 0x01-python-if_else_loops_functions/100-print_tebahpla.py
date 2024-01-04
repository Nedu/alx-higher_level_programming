#!/usr/bin/python3
for character in range(122, 96, -1):
    if character % 2 == 1:
        character -= (97 - 65)
    print("{:c}".format(character), end='')
