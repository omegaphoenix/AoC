from collections import *
import itertools
import sys

def main():
    ans = 0
    state = 'A'
    steps = 12173597
    i = steps
    ls = [0] * (steps * 2 + 1)
    while steps > 0:
        curr = ls[i]
        if state == 'A':
            if curr == 0:
                ls[i] = 1
                i += 1
                state = 'B'
            else:
                ls[i] = 0
                i -= 1
                state = 'C'
        elif state == 'B':
            if curr == 0:
                ls[i] = 1
                i -= 1
                state = 'A'
            else:
                ls[i] = 1
                i += 1
                state = 'D'
        elif state == 'C':
            if curr == 0:
                ls[i] = 1
                i += 1
                state = 'A'
            else:
                ls[i] = 0
                i -= 1
                state = 'E'
        elif state == 'D':
            if curr == 0:
                ls[i] = 1
                i += 1
                state = 'A'
            else:
                ls[i] = 0
                i += 1
                state = 'B'
        elif state == 'E':
            if curr == 0:
                ls[i] = 1
                i -= 1
                state = 'F'
            else:
                ls[i] = 1
                i -= 1
                state = 'C'
        elif state == 'F':
            if curr == 0:
                ls[i] = 1
                i += 1
                state = 'D'
            else:
                ls[i] = 1
                i += 1
                state = 'A'
        else:
            print "Unknown state"
        steps -= 1
    print sum(ls)

main()
