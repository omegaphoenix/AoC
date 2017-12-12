from collections import *
import itertools
import sys

all_zero = set()
all_zero.add('0')

def main():
    ans = 0
    inp = []
    for line in sys.stdin:
        inp.append(line.replace(',',''))
        a = line.replace(',','').strip().split()
        for i in a[2:]:
            if a[0] in all_zero:
                all_zero.add(i)
    print len(inp)
    for _ in range(0, len(inp)):
        for line in inp:
            a = line.strip().split()
            for i in a[2:]:
                if a[0] in all_zero:
                    all_zero.add(i)
    print len(all_zero)

main()
