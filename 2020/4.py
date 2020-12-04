import re
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=4)
raw = puzzle.input_data
data = raw.splitlines()

all_fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

def in_range(val, lo, hi):
    return lo <= val <= hi

def validate_passport(passport):
    for k, v in passport.items():
        if(k == 'byr'):
            if not in_range(int(v),1920,2002): return False
        elif(k == 'iyr'):
            if not in_range(int(v),2010,2020): return False
        elif(k == 'eyr'):
            if not in_range(int(v),2020,2030): return False
        elif(k=='hgt'):
            if v.endswith('cm'):
                if not in_range(int(v[:-2]),150,193): return False
            elif v.endswith('in'):
                if not in_range(int(v[:-2]),59,76): return False
            else:
                return False
        elif(k=='hcl'):
            if not re.fullmatch(r'#[0-9a-f]{6}', v): return False
        elif(k == 'ecl'):
            if v not in ['amb','blu','brn','gry','grn','hzl','oth']: return False
        elif(k == 'pid'):
            if not re.fullmatch(r'[0-9]{9}', v): return False
    return True

part_a = 0
part_b = 0
passport = {}
found_fields = set()
for line in data:
    if(line == ''):
        found_fields = set()
        passport = {}
    else:
        entries = re.findall(r'(\w+):(\S+)', line)
        for field, value in entries:
            passport[field] = value
            found_fields.add(field)
        if(found_fields.issuperset(all_fields)):
            part_a += 1
            found_fields = set()
            if(validate_passport(passport)):
                part_b += 1
            passport = {}

puzzle.answer_a = part_a
puzzle.answer_b = part_b
