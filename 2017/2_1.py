from collections import *
import itertools
import sys

def main():
    sum = 0
    for line in sys.stdin:
        a = list(map(int, line.strip().split()))
        sum += max(a) - min(a)
    print sum

main()
