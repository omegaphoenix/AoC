from collections import *
import itertools
import sys

def main():
    ans = 0
    for line in sys.stdin:
        print line
        a = list(line.strip().split())
        repeated = False
        for i in xrange(0, len(a)):
            for j in xrange(0, len(a)):
                if a[i] == a[j] and i != j:
                    repeated = True
        if repeated == False:
            ans += 1
    print ans

main()
