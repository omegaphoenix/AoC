from collections import *
import itertools
import sys


def spiral(steps):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_index = 0
    coord = (0, 0)
    prev_coord = (0, 0)
    store = {coord: 1}
    steps_left = 1
    count = 1
    while store[prev_coord] < steps:
        store[coord] = calc_val(store, coord)
        print "store"
        print coord
        print store[coord]
        if steps_left == 0:
            dir_index += 1
            dir_index %= 4
            if dir_index % 2 == 0:
                count += 1
            steps_left = count

        prev_coord = coord
        coord = (coord[0] + dirs[dir_index][0], coord[1] + dirs[dir_index][1])
        # steps -= 1
        steps_left -= 1

def calc_val(store, coord):
    if coord ==(0, 0):
        return 1
    val = 0
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                pass
            else:
                x = coord[0] + i - 1
                y = coord[1] + j - 1
                if ((x, y) in store):
                    val += store[(x, y)]
    return val


def main():
    ans = 0
    for line in sys.stdin:
        val = int(line)
        print spiral(val)
    print ans

main()
