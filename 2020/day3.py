def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [x.strip() for x in lines]


TREE = '#'
def count_trees(terrain, right_steps, down_steps):
    (curr_x, curr_y) = (0, 0)
    trees = 0
    while curr_y < len(terrain):
        line = terrain[curr_y]
        if line[curr_x] == TREE:
            trees += 1
        curr_y += down_steps
        curr_x = (curr_x + right_steps) % len(line)
    return trees

def main():
    filename = "day3_input"
    terrain = read_file(filename)
    print("Part 1", count_trees(terrain, 3, 1))
    print("Part 2",
            count_trees(terrain, 1, 1)
            * count_trees(terrain, 3, 1)
            * count_trees(terrain, 5, 1)
            * count_trees(terrain, 7, 1)
            * count_trees(terrain, 1, 2)
            )

main()

