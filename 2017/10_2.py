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
    for line in sys.stdin:
        skip_size = 0
        a = list(map(ord, line.strip()))
        print a
        b = a + [17, 31, 73, 47, 23]
        for _ in range(64):
            for i in b:
                curr = reverse(ans, i, curr)
                ans = (ans + i + skip_size) % len(curr)
                skip_size += 1
        c = range(16)
        for i in range(16):
            c[i] = 0
            for j in range(16):
                c[i] ^= curr[16*i + j]
    print map(hex, c)
    str_ans = ""
    for s in map(hex, c):
        if len(s[2:]) == 2:
            str_ans += s[2:]
        else:
            str_ans += '0' + s[2:]
    print len(str_ans)
    print str_ans


main()
