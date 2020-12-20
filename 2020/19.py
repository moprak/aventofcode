import re
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=19)
raw = puzzle.input_data

rules, data = raw.split('\n\n')

rules = rules.replace('"a"', 'a')
rules = rules.replace('"b"', 'b')

ruleset = {}
for rule in rules.splitlines():
    p1, p2 = rule.split(': ')
    ruleset[p1] = p2

parsed_rules = {}
part2 = False
def get_rule(num):
    if part2:
        if num == '8':
            rule = get_rule('42')+'+'
            parsed_rules[num] = rule
        elif num == '11':
            r42 = get_rule('42')
            r31 = get_rule('31')
            rule = '(' + '|'.join(f'{r42}{{{n}}}{r31}{{{n}}}' for n in range(1,10)) +')'
            parsed_rules[num] = rule

    if num in parsed_rules:
        return parsed_rules[num]

    rule = ruleset[num]
    if rule in ('a','b'):
        parsed_rules[num] = rule
    else:
        options = rule.split(' | ')
        res = []
        for opt in options:
            nums = opt.split()
            res.append(''.join(get_rule(num) for num in nums))
        parsed_rules[num] = '(' + '|'.join(res) +')'
    return parsed_rules[num]

ans = 0
regex = get_rule('0')
for line in data.splitlines():
    if( re.fullmatch(regex,line) ): ans += 1

print(ans)

part2 = True
parsed_rules = {}

ans = 0
regex = get_rule('0')
for line in data.splitlines():
    if( re.fullmatch(regex,line) ): ans += 1

print(ans)
