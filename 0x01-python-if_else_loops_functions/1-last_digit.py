#!/usr/bin/python3
import random
result = random.randint(-10000, 10000)
last_digit = abs(result) % 10
exep = -last_digit
if result <= -1:
    print(f"Last digit of {result} is {exep} and is less than 6 and not 0")
elif last_digit > 5:
    print(f"Last digit of {result} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {result} is {last_digit} and is 0")
else:
    print(f"Last digit of {result} is {last_digit} and is less than 6 and not 0")
