#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    else:
        sum = 0
        str_list = []
        for i in roman_string.upper():
            str_list.append(i)

        for letter in str_list:
            if letter == "I":
                sum = sum + 1
            elif letter == "V":
                sum = sum + 5
            elif letter == "X":
                sum = sum + 10
            elif letter == "L":
                sum = sum + 50
            elif letter == "C":
                sum = sum + 100
            elif letter == "D":
                sum = sum + 500
            elif letter == "M":
                sum = sum + 1000

        return sum
