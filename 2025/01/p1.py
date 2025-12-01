#!python

from pprint import pprint


filename = "ex_in.txt"
filename = "input.txt"

rot_arr = []

# load from file
with open(filename) as file:
  for line in file:
    rot_dir_right = True
    curr_rot = 0
    for i in range(0, len(line)):
      if line[i] == '\n':
        continue
      elif line[i] == 'L':
        rot_dir_right = False
      elif line[i] == 'R':
        rot_dir_right = True
      else:
        curr_rot *= 10
        curr_rot += int(line[i])

    if not rot_dir_right:
      curr_rot = -abs(curr_rot)

    rot_arr.append(curr_rot)

pprint(rot_arr)


def spin_curr_num(n, is_right):
  #print(f'spin_curr_num(n={n}, is_right={is_right}) ->', end='')
  if is_right:
    while(n > 99):
      n -= 100
  elif not is_right and n < 0:
    while(n < -99):
      n += 100
    if n < 0:
      n = 100-abs(n)
  #print(n)
  return n

curr_num = 50
ptr_at_zero = 0

for rot in rot_arr:
  # print curr
  print(f'{curr_num} {rot} -> ', end="")
  if rot > 0:
    curr_num = spin_curr_num(curr_num+rot, True)
  else: # rot < 0
    curr_num = spin_curr_num(curr_num+rot, False)
  print(curr_num)

  # count password
  if curr_num == 0:
    ptr_at_zero += 1

print(f'PW: {ptr_at_zero}')