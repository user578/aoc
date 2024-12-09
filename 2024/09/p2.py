#!python

from pprint import pprint



#filename = "ex_in_1.txt"
#filename = "ex_in_2.txt"
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


def find_first_free_space(bl, bl_len, lim):
  if bl_len == 0:
    return -1
  curr_len = 0
  i_st = 0
  for i in range(0, len(bl)):
    if i == lim:
      return -1
    if curr_len == bl_len:
      return i_st
    if curr_len == 0:
      i_st = i
    if str(bl[i]) == '.':
      curr_len += 1
      continue
    else:
      curr_len = 0
      continue
  return -1



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

print_bl(bl)
print(f'bl len (zz): {len(bl)}')



# iterate over last full data blocks
curr_len = 0
curr_data = ''
first_id = len(bl)-1
cnt_moved = 0
for i in range(len(bl)-1, -1, -1):
  # print('+')
  if str(bl[i]) == '.' or bl[i] != curr_data:
    ipl = find_first_free_space(bl, curr_len, first_id)
    # print(f'find_first_free_space: {ipl}')
    # print(f'curr_len: {curr_len}')
    # print(f'curr_data: {curr_data}')
    # print(f'first_id: {first_id}')
    if ipl >= 0:
      # place data
      for j in range(ipl, ipl+curr_len):
        # print(f'pl data id: {j}')
        bl[j] = curr_data
      # place free space
      for j in range(first_id, first_id-curr_len, -1):
        # print(f'pl free sp id: {j}')
        bl[j] = '.'
      cnt_moved += 1
      print(f'moved (zz): {cnt_moved}')
    if str(bl[i]) == '.':
      curr_len = 0
    else:
      first_id = i
      curr_len = 1
    curr_data = bl[i]
    # print_bl(bl)
    continue
  else:
    curr_len += 1


print(f'checksum (zz): {checksum(bl)}')
