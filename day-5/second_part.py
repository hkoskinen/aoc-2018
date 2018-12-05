filename = 'input.txt'

# first read the entire content from the input file
content = ''
with open(filename) as file_obj:
  content = file_obj.read().strip()

print('Processing... This will take a minute or two.')

def react_polymer(content):
  units_remaining = len(content)
  loop_count = 0
  new_content = ''
  while loop_count < 100000:
    for i in range(0, len(content)):
      if i + 1 == len(content):
        continue
      a = content[i]
      b = content[i+1]

      if a.lower() == b.lower():
        # same letter
        if a == b:
          # same letter and same case
          pass
        else:
          # same letter and different case -> remove
          new_content = content[:i] + content[i + 2:]
          if units_remaining > len(new_content):
            units_remaining = len(new_content)
          break
      else:
        # different letter
        pass

    content = new_content
    new_content = ''
    loop_count += 1

  return units_remaining

alpha = list('abcdefghijklmnopqrstuvwxyz')
polymer_sizes = []
for c in alpha:
  upper_c = c.upper()
  removed_content = content.replace(upper_c, '').replace(c, '')
  react_polymer_result = react_polymer(removed_content)
  polymer_sizes.append(react_polymer_result)
  #print('Removed all ', upper_c, '/', c ,' units. Remaining units after fully reacting the polymer ', react_polymer_result, '.', sep='')

print('Remaining units after fully reacting the polymer ', sorted(polymer_sizes)[0], '.', sep='')