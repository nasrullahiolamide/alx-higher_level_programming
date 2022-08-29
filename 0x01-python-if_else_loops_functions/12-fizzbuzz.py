#!/usr/bin/python3
def fizzbuzz():
    a, b = 1, 100
    for i in range(a, b):
        if i % (3*5) == 0:
            print("FizzBuzz", end="")
        elif (i % 3 == 0):
            print("Fizz", end="")
        elif i % 5 == 0:
            print("Buzz", end="")
        else:
            print(i, end="")
        if i == (b - 1):
            break
        else:
            print(", ", end="")
    print()
