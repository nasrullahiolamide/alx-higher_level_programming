#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

string_it = repr(number)
last_string = string_it[-1]
last_digit = int(last_string)
if string_it[0] == "-":
	last_digit = last_digit * -1
# condition
if last_digit < 6 and last_digit != 0:
	print(f"Last digit of {number} is {last_digit} and is less than 6 but not 0")
elif last_digit == 0:
	print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit > 5:
	print(f"Last digit of {number} is {last_digit} and is greater than 5")
