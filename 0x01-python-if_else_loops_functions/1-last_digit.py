#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string_it = repr(number)
last_string = string_it[-1]
last_digit = int(last_string)
print(last_string)
# condition
if last_digit < 6 and last_digit != 0:
	print(f"Last digit of {number} is {last_digit} is less than 6 but not 0")
elif last_digit == 0:
	print(f"Last digit of {number} is {last_digit} and is equal to 0")
elif last_digit > 5:
	print(f"Last digit of {number} is {last_digit} and is greater than 5")
