filename = 'input.txt'

# read file into a list and sort it chronologically
guard_shifts = []
with open(filename) as file_obj:
  for line in file_obj:
    guard_shifts.append(line.rstrip())

guard_shifts = sorted(guard_shifts)

def get_guard_id(action):
  id = None
  if action.startswith('Guard'):
    id = action.split(' ')[1]
  return id

def get_minutes(date):
  return int(date[9:])

guard_timeline_list = []
guard_sleep_count = {}
current_guard = None
falls_asleep = 0
wakes_up = 0

# loop over the sorted list
for idx in range(0, len(guard_shifts)):
  gs = guard_shifts[idx]
  date = gs[6:17]
  action = gs[19:]

  if action.startswith('Guard'):
    guard_timeline = list('............................................................')
    falls_asleep = 0
    wakes_up = 0
    current_guard = get_guard_id(action)
    if current_guard not in guard_sleep_count:
      guard_sleep_count[current_guard] = { 'sleep': 0, 'minutes': {} }

  if action.startswith('falls'):
    falls_asleep = get_minutes(date)

  if action.startswith('wakes'):
    wakes_up = get_minutes(date)
    guard_sleep_count[current_guard]['sleep'] += (wakes_up - falls_asleep)

    for x in range(falls_asleep, wakes_up):
      guard_timeline[x] = '#'
      if x not in guard_sleep_count[current_guard]['minutes']:
        guard_sleep_count[current_guard]['minutes'][x] = 1
      else:
        guard_sleep_count[current_guard]['minutes'][x] += 1

    if idx + 1 < len(guard_shifts):
      next_gs = guard_shifts[idx + 1]
      next_rest = next_gs[19:]
      if next_rest.startswith('Guard'):
        guard_timeline_list.append(current_guard +'\t'+ ''.join(guard_timeline))
    if idx == len(guard_shifts) - 1:
      next_gs = guard_shifts[idx]
      next_rest = next_gs[19:]
      guard_timeline_list.append(current_guard +'\t'+ ''.join(guard_timeline))

# find the guard with highest sleep minutes
guard_most_asleep = [0, -1]
for key in guard_sleep_count:
  if guard_most_asleep[1] < guard_sleep_count[key]['sleep']:
    guard_most_asleep[0] = key
    guard_most_asleep[1] = guard_sleep_count[key]['sleep']

# find the minute that that guard is most frequently in sleep
guard_in_sleep = [-1,-1] # minute, amount
for k in guard_sleep_count[guard_most_asleep[0]]['minutes']:
  if guard_in_sleep[1] < guard_sleep_count[guard_most_asleep[0]]['minutes'][k]:
    guard_in_sleep[0] = k
    guard_in_sleep[1] = guard_sleep_count[guard_most_asleep[0]]['minutes'][k]
#print(guard_in_sleep)

# solution to part 1
print('\nGuard', guard_most_asleep[0], 'has the highest sleep minutes with total of',
  guard_most_asleep[1], 'minutes and is most asleep in minute', guard_in_sleep[0],
  int(guard_most_asleep[0][1:]) * guard_in_sleep[0])

line = [
  'ID\tMinute\n',
  '\t000000000011111111112222222222333333333344444444445555555555\n',
  '\t012345678901234567890123456789012345678901234567890123456789\n'
]
#print(''.join(line))
#for x in sorted(guard_timeline_list):
#  print(x)


# solution to part 2
# find the guard that is most frequently a sleep on the same minute
most_frequent_sleeper = [-1,-1,-1] # id, minutes_slept, the_minute_most_frequently_in_sleep
for guard in guard_sleep_count:
  for k, v in guard_sleep_count[guard]['minutes'].items():
    if most_frequent_sleeper[1] < v:
      most_frequent_sleeper[0] = guard
      most_frequent_sleeper[1] = v
      most_frequent_sleeper[2] = k

print('Guard',most_frequent_sleeper[0], 'was most frequently asleep on minute',
most_frequent_sleeper[2], 'with total of',most_frequent_sleeper[1],'slept minutes.',
int(most_frequent_sleeper[0][1:]) * most_frequent_sleeper[2])