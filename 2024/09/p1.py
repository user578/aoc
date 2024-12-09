#!python

from pprint import pprint



#filename = "ex_in_1.txt"
filename = "ex_in_2.txt"
filename = "input.txt"

dm = []
bl = []
#[<id>, <data>]

# load from file
with open(filename) as file:
  for line in file:
    for i in range(0, len(line)):
      if line[i] == '\n':
        continue
      else:
        dm.append(line[i])

#print(dm)


def print_bl(bl):
  for b in bl:
    print(f'{b}|', end='')
  print()

def is_defragmented(bl):
  cnt = 0
  is_changed = False
  for i in range(len(bl)-1, -1, -1):
    if not is_changed:
      if str(bl[i]) == '.':
        cnt += 1
        continue
      else:
        is_changed = True
    else: # is changed
      if str(bl[i]) == '.':
        print(f'zz {cnt}')
        return False
      else:
        cnt += 1
        continue
  return True


def find_last_data_id(bl):
  for i in range(len(bl)-1, -1, -1):
    if str(bl[i]) != '.':
      return i
    else:
      continue
  return None


def find_first_free_space_id(bl):
  for i in range(0, len(bl)):
    if str(bl[i]) == '.':
      return i
    else:
      continue
  return None


def checksum(bl):
  sum = 0
  for i in range(0, len(bl)):
    if str(bl[i]) == '.':
      continue
    else:
      sum += i*bl[i]
  return sum

# calculate blocks view
is_data = True
curr_id = 0
for i in dm:
  #print(f'i={i}')
  if is_data:
    for j in range(0,int(i)):
      bl.append(curr_id)
    curr_id += 1
    is_data = False
  else: # free space
    for j in range(0,int(i)):
      bl.append('.')
    is_data = True

#print_bl(bl)
print(f'zz {len(bl)}')

while not is_defragmented(bl):
  id_free = find_first_free_space_id(bl)
  id_data = find_last_data_id(bl)
  bl[id_free] = bl[id_data]
  bl[id_data] = '.'
  # print_bl(bl)
  # print('====')

print(f'zz {checksum(bl)}')
