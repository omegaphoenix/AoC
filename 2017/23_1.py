from collections import *
import itertools
import sys

def main():
    ans = 0
    # registers = {'a': 1, '1': 1, 'b': 122699, 'c': 122700, 'f': 0, 'd': 105698, 'e': 105600, 'g': -35827}
    registers = {'a': 1, '1': 1}
    last = 0
    lines = []
    for line in sys.stdin:
        lines.append(line)
    i = 0
    while i >= 0 and i < len(lines):
        if i == 23:
            while registers['g'] < -2:
                registers['g'] += 1
                registers['d'] += 1
        if i == 28:
            print registers
        line = lines[i].strip().split(" ")
        cmd = line[0]
        let = line[1]
        if not let in registers.keys():
            registers[let] = 0
        if cmd == 'set':
            if line[2].islower():
                y = line[2]
                if not (y in registers.keys()):
                    registers[y] = 0
                registers[let] = registers[y]
            else:
                registers[let] = int(line[2])
        if cmd == 'sub':
            if line[2].islower():
                y = line[2]
                if not (y in registers.keys()):
                    registers[y] = 0
                registers[let] -= registers[y]
            else:
                registers[let] -= int(line[2])
        if cmd == 'mul':
            if line[2].islower():
                y = line[2]
                if not (y in registers.keys()):
                    registers[y] = 0
                registers[let] *= registers[y]
            else:
                registers[let] *= int(line[2])
        if cmd == 'jnz' and registers[let] != 0:
            if line[2].islower():
                y = line[2]
                if not (y in registers.keys()):
                    registers[y] = 0
                i += registers[y]
            else:
                i += int(line[2])
        else:
            i += 1

    print registers['h']

main()
