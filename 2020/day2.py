import re

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    res = []
    for line in lines:
        [policy, password] = line.strip().split(": ")
        [lower, upper, key] = re.split('-| ', policy)
        res.append((int(lower) - 1, int(upper) - 1, key, password))
    return res

def validate_password_count(line):
    (lower, upper, key, password) = line
    count = password.count(key)
    return lower <= count and count <= upper

def validate_password_xor(line):
    (lower, upper, key, password) = line
    return (password[lower] == key) != (password[upper] == key)


def main():
    filename = "day2_input"
    passwords = read_file(filename)
    print(sum(map(validate_password_count, passwords)))
    print(sum(map(validate_password_xor, passwords)))

main()


# TODO: Should study regular expressions
