def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines


def calc_acc_before_repeat(instructions):
    line = 0
    run_lines = set()
    acc = 0

    while not line in run_lines:
        if line == len(instructions):
            return (acc, True)

        run_lines.add(line)
        [instruct, value] = instructions[line].split(' ')

        val = int(value[1:])
        sign = value[0]
        if sign == '-':
            val *= -1

        if instruct == "nop":
            line += 1

        if instruct == "jmp":
            line += val

        if instruct == "acc":
            acc += val
            line += 1
    return (acc, False)


def fix_infinite_loop(instructions):
    for idx in range(len(instructions)):
        curr_line = instructions[idx]

        if curr_line[0:3] == "nop":
            instructions[idx] = "jmp" + curr_line[3:]
        elif curr_line[0:3] == "jmp":
            instructions[idx] = "nop" + curr_line[3:]

        (acc, exit) = calc_acc_before_repeat(instructions)
        if exit:
            return acc
        instructions[idx] = curr_line


def main():
    filename = "day8_input"
    instructions = read_input(filename)

    print("Part 1", calc_acc_before_repeat(instructions)[0])
    print("Part 2", fix_infinite_loop(instructions))

main()
