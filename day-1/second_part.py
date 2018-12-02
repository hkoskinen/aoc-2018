filename = 'input.txt'

frequency_changes = []
with open(filename) as file_obj:
  for line in file_obj:
    frequency_changes.append(int(line))

dic = {}
current_freq = 0
running = True

while running:
  for i in range(0, len(frequency_changes)):
    current_freq += frequency_changes[i]

    # if we found the key second time, we know that is a frequency
    # that is reached second time, which is our solution.
    if current_freq in dic:
      print('Found it:', current_freq)
      running = False
      break
    else:
      dic[current_freq] = 1