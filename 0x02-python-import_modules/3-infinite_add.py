#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_ele = sys.argv

    i = 1
    sum = 0
    while i <= (len(arg_ele) - 1):
        sum = sum + int(arg_ele[i])
        i = i + 1
    print(sum)

import hidden_4

print(dir(hidden_4))