from collections import *
import itertools
import sys

def main():
    sum = 0
    for line in sys.stdin:
        a = list(map(int, line.strip().split()))
        for i in range(len(a)):
            for j in range(len(a)):
                if i != j and a[i] % a[j] == 0:
                    sum += a[i] / a[j]
    print sum

main()
