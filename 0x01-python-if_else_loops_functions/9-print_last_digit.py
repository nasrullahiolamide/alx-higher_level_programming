#!/usr/bin/python3
def print_last_digit(number):
    string_it = repr(number)
    last_string = string_it[-1]
    last_digit = int(last_string)

    return last_digit
