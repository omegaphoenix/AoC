import re

def read_file(filename):
    with open(filename) as f:
        file = f.read()
    raw_passports = file.strip().split('\n\n')
    passports = []
    for raw_passport in raw_passports:
        fields = re.split('\n| ', raw_passport)
        passport = {}
        for field in fields:
            [key, value] = field.split(':')
            passport[key] = value
        passports.append(passport)
    return passports

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def validate_passport(passport):
    for field in REQUIRED_FIELDS:
        if not field in passport:
            return False
    return True

VALID_ECL = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
def strict_validate_passport(passport):
    if not validate_passport(passport):
        return False

    birth_year = int(passport['byr'])
    if birth_year < 1920 or birth_year > 2002:
        return False

    issue_year = int(passport['iyr'])
    if issue_year < 2010 or issue_year > 2020:
        return False

    expire_year = int(passport['eyr'])
    if expire_year < 2020 or expire_year > 2030:
        return False

    height = passport['hgt']
    if not ((re.match('\d{3}cm', height) and len(height) == 5 and int(height[0:3]) >= 150 and int(height[0:3]) <= 193)
            or (re.match('\d{2}in', height) and len(height) == 4 and int(height[0:2]) >= 59 and int(height[0:2]) <= 76)):
        return False

    hair_color = passport['hcl']
    if not (re.match('#(\d|[a-f]){6}', hair_color) and len(hair_color) == 7):
        return False

    if not passport['ecl'] in VALID_ECL:
        return False

    if len(passport['pid']) != 9:
        return False
    try:
        int(passport['pid'])
    except ValueError:
        return False

    return True



def main():
    filename = "day4_input"
    passports = read_file(filename)
    print("Part 1", sum(map(validate_passport, passports)))
    print("Part 2", sum(map(strict_validate_passport, passports)))

main()

## TODO: Practice regular expressions
