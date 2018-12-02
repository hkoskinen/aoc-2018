filename = 'input.txt'

box_id_list = []
with open(filename) as file_obj:
  for line in file_obj:
    box_id_list.append(list(line.rstrip())) # remove new line at the end of each line

found = False
for i in range(0, len(box_id_list)):
  word = box_id_list[i]

  for lword in box_id_list:
    #print(''.join(word), '->', ''.join(lword))

    sum = 0
    for l in range(0, len(word)):

      if (word[l] != lword[l]):
        sum += 1
      if sum > 1:
        break

    if sum == 1:
      print('FOUND IT:', ''.join(word), '->', ''.join(lword))

      idx = 0
      for x in range(0, len(word)):
        if word[x] != lword[x]:
          idx = x
          break

      word.pop(idx)
      lword.pop(idx)
      print('Letters common between the two correct box IDs: ', ''.join(word))

      found = True
      break
    else:
      sum = 0

  if found:
    break