#!/usr/bin/python3
a = 0
b = 100
for i in range(a, b):
    if i != (b-1):
        print("{:02d},".format(i), end=' ')
    else:
        print("{:02d}\n".format(i))
