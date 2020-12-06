from collections import *
import itertools
import sys

def strength(ele):
    return 2

def stren(ele):
    return ele[0] + ele[1]

def find_strongest(items, start):
    ans = 0
    stre = 0
    for i in xrange(len(items)):
        clone = items[:]
        curr = items[i]
        val = [0, 0]
        if curr[0] == start:
            clone.pop(i)
            val = find_strongest(clone, curr[1])
            val[0] += strength(curr)
            val[1] += stren(curr)
        clone = items[:]
        if val[0] > ans or (val[0] == ans and val[1] > stre):
            [ans, stre] = val
        if curr[1] == start:
            clone.pop(i)
            val = find_strongest(clone, curr[0])
            val[0] += strength(curr)
            val[1] += stren(curr)
        if val[0] > ans or (val[0] == ans and val[1] > stre):
            [ans, stre] = val
    return [ans, stre]

def main():
    ans = 0
    items = []
    for line in sys.stdin:
        a = list(map(int, line.strip().split('/')))
        items.append(a)
    print find_strongest(items, 0)

main()
