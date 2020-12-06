from collections import *
import itertools
import sys

def main():
    ans = 0
    registers1 = {'1': 1}
    registers2 = {'1': 1}
    last = 0
    lines = []
    for line in sys.stdin:
        lines.append(line)
    i = 0
    j = 0
    queue1 = []
    queue2 = []
    while True:
        stuck1 = False
        stuck2 = False
        if i >= 0 and i < len(lines):
            line = lines[i].strip().split(" ")
            cmd = line[0]
            let = line[1]
            if not let in registers1.keys():
                registers1[let] = 0
            if cmd == 'snd':
                queue2.append(registers1[let])
                ans += 1
            if cmd == 'rcv':
                if len(queue1) > 0:
                    registers1[let] = queue1.pop(0)
                else:
                    stuck1 = True
            if cmd == 'set':
                if line[2].islower():
                    y = line[2]
                    if not (y in registers1.keys()):
                        registers1[y] = 0
                    registers1[let] = registers1[y]
                else:
                    registers1[let] = int(line[2])
            if cmd == 'add':
                if line[2].islower():
                    y = line[2]
                    if not (y in registers1.keys()):
                        registers1[y] = 0
                    registers1[let] += registers1[y]
                else:
                    registers1[let] += int(line[2])
            if cmd == 'mul':
                if line[2].islower():
                    y = line[2]
                    if not (y in registers1.keys()):
                        registers1[y] = 0
                    registers1[let] *= registers1[y]
                else:
                    registers1[let] *= int(line[2])
            if cmd == 'mod':
                if line[2].islower():
                    y = line[2]
                    if not (y in registers1.keys()):
                        registers1[y] = 0
                    registers1[let] = registers1[let] % registers1[y]
                else:
                    registers1[let] = registers1[let] % int(line[2])
            if cmd == 'jgz' and registers1[let] > 0:
                i += int(line[2])
            else:
                i += 1

        if j >= 0 and j < len(lines):
            line = lines[j].strip().split(" ")
            cmd = line[0]
            let = line[1]
            if not let in registers2.keys():
                registers2[let] = 0
            if cmd == 'snd':
                queue1.append(registers2[let])
            if cmd == 'rcv':
                if len(queue2) > 0:
                    registers2[let] = queue2.pop(0)
                else:
                    stuck2 = True
            if cmd == 'set':
                if line[2].islower():
                    y = line[2]
                    if not (y in registers2.keys()):
                        registers2[y] = 0
                    registers2[let] = registers2[y]
                else:
                    registers2[let] = int(line[2])
            if cmd == 'add':
                if line[2].islower():
                    y = line[2]
                    if not (y in registers2.keys()):
                        registers2[y] = 0
                    registers2[let] += registers2[y]
                else:
                    registers2[let] += int(line[2])
            if cmd == 'mul':
                if line[2].islower():
                    y = line[2]
                    if not (y in registers2.keys()):
                        registers2[y] = 0
                    registers2[let] *= registers2[y]
                else:
                    registers2[let] *= int(line[2])
            if cmd == 'mod':
                if line[2].islower():
                    y = line[2]
                    if not (y in registers2.keys()):
                        registers2[y] = 0
                    registers2[let] = registers2[let] % registers2[y]
                else:
                    registers2[let] = registers2[let] % int(line[2])
            if cmd == 'jgz' and registers2[let] > 0:
                j += int(line[2])
            else:
                j += 1
        if stuck1 and stuck2:
            break
        else:
            print j
            print registers1
            print registers2

    print ans

main()
