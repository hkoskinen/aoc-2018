filename = 'input.txt'

def parse_claims(file_obj):
  claims = {}
  for line in file_obj:
    claim_parts = line.rstrip().split(' ')
    id = claim_parts[0].replace('#', '')
    pos = claim_parts[2].replace(':','').split(',')
    size = claim_parts[3].split('x')

    claims[id] = {
      'x': int(pos[0]),
      'y': int(pos[1]),
      #'w': int(size[0]),
      #'h': int(size[1])
      'x2': int(pos[0]) + int(size[0]),
      'y2': int(pos[1]) + int(size[1])
    }
  return claims

claims = {}
with open(filename) as file_obj:
  claims = parse_claims(file_obj)

# create the grid
size = 1000
grid = []
for row_idx in range(0, size):
  row = []
  for col_idx in range(0, size):
    row.append(0)
  grid.append(row)

# put each claim into the grid
for claim in claims:
  x1 = claims[claim]['x']
  y1 = claims[claim]['y']
  x2 = claims[claim]['x2']
  y2 = claims[claim]['y2']

  for row in range(y1, y2):
    for col in range(x1, x2):
      grid[row][col] += 1

# go over the grid again to see which claim square doesn't overlap
for claim in claims:
  x1 = claims[claim]['x']
  y1 = claims[claim]['y']
  x2 = claims[claim]['x2']
  y2 = claims[claim]['y2']
  print('Checking claim:', claim)

  all_ones = True
  for row in range(y1, y2):
    for col in range(x1, x2):
      if grid[row][col] != 1:
        all_ones = False
        break

  if all_ones:
    print('Found the claim ID that doesn\'t overlap:', claim)
    break