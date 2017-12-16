from collections import *
import itertools
import sys

def main():
    ans = 0
    startA = 634
    startB = 301
    factorA = 16807
    factorB = 48271
    div = 2147483647
    matter = 2**16
    for i in xrange(5000000):
        startA *= factorA
        startA %= div
        while startA % 4 != 0:
            startA *= factorA
            startA %= div
        startB *= factorB
        startB %= div
        while startB % 8 != 0:
            startB *= factorB
            startB %= div
        if (startA % matter) == (startB % matter):
            ans += 1
    print ans

main()
