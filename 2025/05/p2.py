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
# print(len(ranges))
# exit(1)
# print()
# print(ids)
# exit(1)


def find_non_intersect_new_ranges(newr, oldr):
  # exact same
  if newr[0] == oldr[0] and newr[1] == oldr[1]:
    return []
  # left intersect
  elif newr[0] < oldr[0] and newr[1] >= oldr[0] and newr[1] <= oldr[1]:
    return [[newr[0], oldr[0]-1]]
  # right intersect
  elif newr[0] >= oldr[0] and newr[0] <= oldr[1] and newr[1] > oldr[1]:
    return [[oldr[1]+1, newr[1]]]
  # full inner interact
  elif newr[0] < oldr[0] and newr[1] > oldr[1]:
    return [[newr[0], oldr[0]-1],
            [oldr[1]+1, newr[1]]]
  else:
    return []

def is_duplicate(newr, oldr):
  if newr[0] == oldr[0] and newr[1] == oldr[1]:
    return True
  else:
    return False

#print(find_non_intersect_new_ranges([0,1], [2,4]))


# ranges=[
#   [0,8], [0,8], [0,8]
# ]

curr_item = 0
while(True):
  new_ranges = []
  is_dupl_bool = False
  #print(f'curr_item={curr_item}')
  #pprint(ranges)
  for ri, r in enumerate(ranges):
    #print(f'ri={ri}')
    if ri != curr_item:
      # print(r)
      new_ranges = find_non_intersect_new_ranges(ranges[curr_item], r)
      if len(new_ranges) > 0:
        print(f'Found new ranges ({curr_item} {ri}): {new_ranges}')
        # print(ranges[curr_item])
        # print(r)
        ranges.pop(curr_item)
        ranges += new_ranges
        break
      elif is_duplicate(ranges[curr_item], r):
        ranges.pop(curr_item)
        is_dupl_bool = True
        break
  # curr_item += 1
  # if curr_item == len(ranges):
  #   break
  if curr_item == len(ranges)-1:
    break
  if len(new_ranges) > 0 or is_dupl_bool:
    curr_item = 0
  else:
    curr_item += 1
  #input()

#pprint(ranges)
# exit(0)

sum = 0
for r in ranges:
  sum += r[1]-(r[0]-1)

print(sum)
