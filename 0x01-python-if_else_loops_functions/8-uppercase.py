#!/usr/bin/python3
def uppercase(string):
    string_new = ""
    for character in string:
        uppercaseChar = character
        if ord(uppercaseChar) >= 97 and ord(uppercaseChar) <= 122:
            uppercaseChar = ord(uppercaseChar) - 32
        else:
            uppercaseChar = ord(uppercaseChar)
        string_new += "%c" % uppercaseChar
    print("{:s}".format(string_new))
