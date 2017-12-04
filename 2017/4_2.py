from collections import *
import itertools
import sys

def anagrams(s1, s2):
    def sort(s):
        return sorted(s.lower())
    return sort(s1) == sort(s2)

def main():
    ans = 0
    for line in sys.stdin:
        print line
        a = list(line.strip().split())
        repeated = False
        for i in xrange(0, len(a)):
            for j in xrange(0, len(a)):
                if anagrams(a[i], a[j]) and i != j:
                    repeated = True
        if repeated == False:
            ans += 1
    print ans

main()
