#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number >= 0:
    lastDigit = number % 10
else:
    lastDigit = ((number * -1) % 10) * -1

result = "Last digit of %d is %d and is" % (number, lastDigit)

if lastDigit == 0:
    print(result, "0")
elif lastDigit > 5:
    print(result, "greater than 5")
else:
    print(result, "less than 6 and not 0")
