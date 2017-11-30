INPUT = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5".split(", ")

coord = (0, 0)
direction = 0
MOVE = [(0, 1), (1, 0), (0,-1), (-1,0)]
visited = set()
done = False

def tupleadd(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]+y[i])
    return tuple(z)

for cmd in INPUT:
    if done:
        break
    if cmd[0] == 'R':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1 + 4) % 4
    dist = int(cmd[1:])
    for _ in xrange(dist):
        coord = tupleadd(coord, MOVE[direction])
        if coord in visited:
            print coord
            print abs(coord[0]) + abs(coord[1])
            done = True
            break
        visited.add(coord)

