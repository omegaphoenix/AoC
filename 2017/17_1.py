from collections import *
import itertools
import sys

def main():
    ans = 0
    steps = 303
    ls = [0]
    curr_idx = 0
    for x in xrange(2017):
        y = x + 1
        curr_idx = ((curr_idx + steps) % len(ls)) + 1
        ls = ls[:curr_idx] + [y] + ls[curr_idx:]
    print ls[ls.index(2017) + 1]

main()
