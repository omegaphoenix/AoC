from collections import *
import itertools
import sys

def reverse(cur_idx, leng, lst):
    for i in range(int(leng/2)):
        idx = (i + cur_idx) % len(lst)
        other_idx = (leng + cur_idx - i - 1) % len(lst)
        temp = lst[idx]
        lst[idx] = lst[other_idx]
        lst[other_idx] = temp
    return lst


def main():
    ans = 0
    curr = range(256)
    print curr
    for line in sys.stdin:
        print line
        skip_size = 0
        a = list(map(int, line.strip().split(',')))
        for i in a:
            print i
            curr = reverse(ans, i, curr)
            ans = (ans + i + skip_size) % len(curr)
            skip_size += 1
            print curr
    print curr[0]*curr[1]

main()
