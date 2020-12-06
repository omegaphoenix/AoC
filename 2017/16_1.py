from collections import *
import itertools
import sys


def main():
    ans = 0
    letters = list("abcdefghijklmnop")
    def find(c):
        return letters.index(c)
    tot = len(letters)
    for line in sys.stdin:
        print line
        a = list(line.strip().split(','))
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
    print letters

main()
