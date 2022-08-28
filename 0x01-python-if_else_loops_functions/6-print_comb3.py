#!/usr/bin/python3
a, b = 0, 0
for i in range(0, 10):
    for s in range(0, 10):
        if i != s and (repr(i) + repr(s)) < (repr(s) + repr(i)):
            if (repr(i) + repr(s)) == ('89'):
                print(f"{i}{s}")
                break
            print(f"{i}{s}, ", end="")
