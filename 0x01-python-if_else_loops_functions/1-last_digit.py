#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is { abs(number) % 10}", end="")

if (abs(number) % 10 > 5):
    print(" and is greater than 5",end="")
elif (abs(number) % 10 < 6):
    print("and is less than 5",end="")
    
if abs(number) % 10 == 0:
    print("and is 0")
else:
    print("and not 0")

