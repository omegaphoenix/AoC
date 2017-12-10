from collections import *
import itertools
import sys

def main():
    ans = 0
    inp = ""
    nested = 1
    in_garb = False
    for line in sys.stdin:
        inp = line
    i = 0
    while i < len(line):
        c = line[i]
        if in_garb:
            if c == "!":
                i += 1
            else:
                if c == ">":
                    in_garb = False
                else:
                    ans += 1

        else:
            if c == "{":
                nested += 1
            if c == "}":
                nested -= 1
            if c == "<":
                in_garb = True
        i += 1


    print ans

main()
