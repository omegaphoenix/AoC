from collections import *
import itertools
import sys

def main():
    ans = 0
    seen = []
    for line in sys.stdin:
        a = list(map(int, line.strip().split()))
        print a
        while not a in seen:
            seen.append(a[:])
            max_idx = a.index(max(a))
            count = max(a)
            a[max_idx] = 0
            i = (max_idx + 1) % len(a)
            while count > 0:
                count -= 1
                a[i] += 1
                i = (i + 1) % len(a)
            ans += 1
        print ans - seen.index(a)

main()
