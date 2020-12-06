from collections import *
import itertools
import sys

def main():
    ans = 1
    steps = 303
    ls = [0]
    curr_idx = 0
    size = 1
    for x in xrange(50000000):
        y = x + 1
        curr_idx = ((curr_idx + steps) % size) + 1
        size += 1
        if curr_idx == 1:
            ans = y
            print y
    print y

main()
