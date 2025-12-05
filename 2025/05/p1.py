#!python

from pprint import pprint


filename = "ex_in.txt"
filename = "input.txt"

ranges = []
ids = []


# load lines from file
is_load_ranges = True
with open(filename) as file:
  for line in file:
    r = []
    n = ''
    if is_load_ranges:
      for i in range(0, len(line)):
        if line[i] == '\n':
          if len(r) == 0:
            is_load_ranges = False
            continue
          else:
            r.append(int(n))
            continue
        elif line[i] == '-':
          r.append(int(n))
          n = ''
        else:
          n += line[i]
      if is_load_ranges:
        ranges.append(r)
    else: # load ids
      ids.append(int(line))


# pprint(ranges)
# print()
# print(ids)

cnt_fresh = 0
for id in ids:
  #print(f'====\nid={id}')
  is_id_fresh = False
  for r in ranges:
    #print(f'r={r}')
    if id >= r[0] and id <= r[1]:
      is_id_fresh = True
      #print(f'is fresh!')
      break
  if is_id_fresh:
    cnt_fresh += 1

print(cnt_fresh)