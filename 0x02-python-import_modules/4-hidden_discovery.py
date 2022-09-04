#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
        names = dir(hidden_4)

        i = 1
        while i <= (len(names) - 1):
                if names[i][0:2] != "__":
                        print(names[i])
                i = i + 1
