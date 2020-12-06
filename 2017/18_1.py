from collections import *
import itertools
import sys

def main():
    ans = 0
    registers = {}
    last = 0
    lines = []
    for line in sys.stdin:
        lines.append(line)
    i = 0
    while True:
        line = lines[i].strip().split(" ")
        cmd = line[0]
        let = line[1]
        if not let in registers.keys():
            registers[let] = 0
        if cmd == 'snd':
            last = registers[let]
        if cmd == 'rcv':
            if registers[let] != 0:
                print last
                break
        if cmd == 'set':
            if line[2].islower():
                y = line[2]
                if not (y in registers.keys()):
                    registers[y] = 0
                registers[let] = registers[y]
            else:
                registers[let] = int(line[2])
        if cmd == 'add':
            if line[2].islower():
                y = line[2]
                if not (y in registers.keys()):
                    registers[y] = 0
                registers[let] += registers[y]
            else:
                registers[let] += int(line[2])
        if cmd == 'mul':
            if line[2].islower():
                y = line[2]
                if not (y in registers.keys()):
                    registers[y] = 0
                registers[let] *= registers[y]
            else:
                registers[let] *= int(line[2])
        if cmd == 'mod':
            if line[2].islower():
                y = line[2]
                if not (y in registers.keys()):
                    registers[y] = 0
                registers[let] = registers[let] % registers[y]
            else:
                registers[let] = registers[let] % int(line[2])
        if cmd == 'jgz' and registers[let] > 0:
            i += int(line[2])
        else:
            i += 1

    print ans

main()
