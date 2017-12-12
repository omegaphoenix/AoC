from collections import *
import itertools
import sys

def main():
    ans = 0
    inp = []
    for line in sys.stdin:
        inp.append(line.replace(',',''))
    all_zero = set()
    while len(inp) > 0:
        all_zero.add(inp[0].strip().split()[0])
        ans += 1
        for x in range(0, len(inp)):
            for line in inp:
                a = line.strip().split()
		if a[0] in all_zero:
		    for i in a[2:]:
                        all_zero.add(i)

	i = 0
        while i < len(inp):
            if inp[i].strip().split()[0] in all_zero:
                inp.pop(i)
            else:
                i += 1
    print ans

main()
