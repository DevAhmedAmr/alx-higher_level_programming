#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
is_negative = number < 0
last_digit = abs(number) % 10

if is_negative == True:
    last_digit *= -1

print(f"Last digit of {number} is { last_digit }", end=" ")

if (last_digit  > 5):
    print(" and is greater than 5")
elif (last_digit  < 6):
    print("and is less than 5")

