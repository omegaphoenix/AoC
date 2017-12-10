from collections import *
import itertools
import sys

def main():
    ans = 0
    all_reg = dict()
    input = []
    vals = []
    for line in sys.stdin:
        a = list(line.strip().split())
        all_reg[a[0]] = 0
        input.append(a)
    for a in input:
        statement = "all_reg['" + a[4] + "'] " + a[5] + a[6]
        if eval(statement):
            if a[1] == "inc":
                all_reg[a[0]] += int(a[2])
            else:
                all_reg[a[0]] -= int(a[2])
            vals.append(all_reg[a[0]])
    print max(all_reg.values())
    print max(vals)

main()
