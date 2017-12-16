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


def knot_hash(inputs):
    lens = [ord(x) for x in inputs.rstrip()]
    lens.extend([17,31,73,47,23])
    nums = [x for x in range(0,256)]
    pos = 0
    skip = 0
    for _ in range(64):
        for l in lens:
            to_reverse = []
            for x in range(l):
                n = (pos + x) % 256
                to_reverse.append(nums[n])
            to_reverse.reverse()
            for x in range(l):
                n = (pos + x) % 256
                nums[n] = to_reverse[x]
            pos += l + skip
            pos = pos % 256
            skip += 1
    dense = []
    for x in range(0,16):
        subslice = nums[16*x:16*x+16]
        dense.append('%02x'%reduce((lambda x,y: x ^ y),subslice))
    scale = 16 ## equals to hexadecimal

    num_of_bits = 128

    hexa = (''.join(dense))
    return bin(int(hexa, scale))[2:].zfill(num_of_bits)



def main():
    ans = []
    inputs = "jxqlasbh"
    for i in xrange(128):
        curr = inputs + "-" + str(i)
        ans.append(knot_hash(curr))
    temp = ""
    for x in ans:
        temp += x
    count = 0
    while temp.count('1') > 0:
        i = 0
        while ans[i].count('1') == 0:
            i += 1
            if i == 128:
                print count
                break
        j = ans[i].find('1')
        queue = [(i, j)]
        while len(queue) > 0:
            curr = queue.pop(0)
            x = curr[0]
            y = curr[1]
            if x >= 0 and x < 128 and y >= 0 and y < 128 and ans[x][y] == '1':
                ans[x] = ans[x][:y] + "0" + ans[x][y+1:]
                queue.append((x + 1,y))
                queue.append((x,y + 1))
                queue.append((x - 1,y))
                queue.append((x,y - 1))
        for x in ans:
            temp += x
        count += 1
    print count

main()

