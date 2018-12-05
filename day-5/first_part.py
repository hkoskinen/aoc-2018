filename = 'input.txt'

# first read the entire content from the input file
content = ''
with open(filename) as file_obj:
  content = file_obj.read().strip()
#print(content, len(content))

print('Processing... This will take a minute or two.')

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
        #print(new_content, len(new_content))
        #print()
        if units_remaining > len(new_content):
          units_remaining = len(new_content)
        break
    else:
      # different letter
      pass

  content = new_content
  new_content = ''
  loop_count += 1

print('Remaining units after fully reacting the polymer ', units_remaining, '.', sep='')