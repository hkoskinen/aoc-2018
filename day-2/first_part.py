filename = 'input.txt'

box_id_list = []
with open(filename) as file_obj:
  for line in file_obj:
    box_id_list.append(line.rstrip()) # remove new line at the end of each line

def calculate_checksum(id_list):
  # The final checksum for the list of box id's is calculated by
  # multiplying twos by threes. twos * threes = checksum
  id_counts = {
    'twos': 0,
    'threes': 0
  }

  def calculate_letters(id):
    d = {}
    letter_list = list(id) # split id string into letter list
    for l in letter_list:
      if l in d:
        d[l] += 1
      else:
        d[l] = 1

    for key in d:
      if d[key] == 2:
        id_counts['twos'] += 1
        break
    for key in d:
      if d[key] == 3:
        id_counts['threes'] += 1
        break

  for id in id_list:
    calculate_letters(id)

  return id_counts['twos']  * id_counts['threes']

print(calculate_checksum(box_id_list)) # 7872