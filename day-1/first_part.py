filename = 'input.txt'

result = 0
with open(filename) as file_obj:
  for line in file_obj:
    result += int(line)

print(result) # 497