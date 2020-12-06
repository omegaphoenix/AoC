def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [int(x) for x in lines]


# O(n)
def find_two_sum(target, values):
    existing = set();

    for val in values:
        if (target - val) in existing:
            return (target - val, val)
        existing.add(val)

    raise Error("No values sum up to target")


# O(n^2)
def find_three_sum(target, values):
    existing = set(values);
    num_vals = len(values)

    for i in range(0, num_vals):
        x = values[i]
        for j in range(i + 1, num_vals):
            y = values[j]
            complement = target - x - y
            if complement in existing:
                return (x, y, complement)

    raise Error("No values sum up to target")


def main():
    filename = "day1_input"
    input_values = read_input(filename)

    (x, y) = find_two_sum(2020, input_values)
    print("Part 1", x, y, x * y)

    (x, y, z) = find_three_sum(2020, input_values)
    print("Part 2", x, y, z, x * y * z)

main()
