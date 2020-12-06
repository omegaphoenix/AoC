from collections import *
import itertools
import sys

def update(a, letters):
    def find(c):
        return letters.index(c)
    tot = len(letters)
    for x in a:
        m = x[0]
        if m == 's':
            n = int(x[1:])
            letters = letters[(tot - n):] + letters[:(tot - n)]
        if m == 'x':
            vals = map(int, x[1:].split('/'))
            temp = letters[vals[0]]
            letters[vals[0]] = letters[vals[1]]
            letters[vals[1]] = temp
        if m == 'p':
            vals = map(find, x[1:].split('/'))
            temp = letters[vals[0]]
            letters[vals[0]] = letters[vals[1]]
            letters[vals[1]] = temp
    return letters

def main():
    ans = 0
    letters = list("abcdefghijklmnop")
    clone = list("abcdefghijklmnop")
    billion = 1000000000
    num_repeat = 0
    for line in sys.stdin:
        a = list(line.strip().split(','))
        for i in xrange(billion):
            if i != 0 and letters == clone:
                num_repeat = i
                break
            letters = update(a, letters)
        print num_repeat
        for i in xrange(billion % num_repeat):
            letters = update(a, letters)
    print letters

main()
