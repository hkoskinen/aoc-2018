filename = 'input.txt'

instructions = []
lefts = []
rights = []
with open(filename) as file_obj:
  for line in file_obj:
    l = line.strip().split(' ')
    instructions.append([l[1], l[7]])
    lefts.append(l[1])
    rights.append(l[7])

lefts = sorted(set(lefts))
rights = sorted(set(rights))

# find start letters
starts = []
for s in lefts:
  if s not in rights:
    starts.append(s)
starts = sorted(starts)

# fill the missing dictionary
col = {}
for k in rights:
  col[k] = {
    'missing':[]
  }
  for pair in instructions:
    if pair[1] == k:
      col[k]['missing'].append(pair[0])

final = []
while len(starts) > 0:
  gathered = []
  for c in col:
    if starts[0] in col[c]['missing']:
      col[c]['missing'].remove(starts[0])
      if len(col[c]['missing']) == 0:
        gathered.append(c)

  # now the 'start' is used, we need to add it to the pile
  final.append(starts[0])

  # then we need new start
  starts.remove(starts[0])
  starts.extend(gathered)
  starts = sorted(starts)

print(''.join(final))

# HPDTNXYLOCGEQSIMABZKRUW = 23
# HPDTNXYLOCGEQSIMABZKRUWVFJ = 26

# normal enlish alphabet count is 26 A-Z