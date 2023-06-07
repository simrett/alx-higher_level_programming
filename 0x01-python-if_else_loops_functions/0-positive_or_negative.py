#!/usr/bin/python3
import random
result = random.randint(-10, 10)
if result > 0:
    print("{} is positive".format(result))
elif result == 0:
    print("{} is zer".format(result))
else:
    print("{} is negative".format(result))
