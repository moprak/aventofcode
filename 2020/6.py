f = open('6.in')
part_a = 0
part_b = 0
family_answers = []
for line in f.read().splitlines():
    if line == '':
        part_a += len(set.union(*family_answers))
        part_b += len(set.intersection(*family_answers))
        family_answers = []
    else:
        person_answers = set([c for c in line])
        family_answers.append(person_answers)
