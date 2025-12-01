#!python

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


def spin_curr_num(n, rot, is_right):
  print(f'spin_curr_num(n={n}, rot={rot}, is_right={is_right})')
  ptr_at_zero_cnt = 0
  # check if sum of n and rot goes over 0 at least once
  if not is_right and n+rot < 1 and n != 0:
    ptr_at_zero_cnt += 1
    print(f'PTR++: not is_right and n+rot < 1')

  n = n+rot

  # calc
  if is_right:
    while(n > 99):
      n -= 100
      ptr_at_zero_cnt += 1
      print(f'PTR++: while R')
  elif not is_right and n < 0:
    while(n < 0):
      if n < -99:
        n += 100
        ptr_at_zero_cnt += 1
        print(f'PTR++: while L')
      else:
        n = 100-abs(n)
  #print(n)
  return n, ptr_at_zero_cnt

curr_num = 50
ptr_at_zero = 0

for rot in rot_arr:
  # print curr
  print(f'#{curr_num} {rot}')
  if rot > 0:
    curr_num, ptr_at_zero_cnt = spin_curr_num(curr_num, rot, True)
  else: # rot < 0
    curr_num, ptr_at_zero_cnt = spin_curr_num(curr_num, rot, False)
  print(f'-> {curr_num}')

  # count password
  ptr_at_zero += ptr_at_zero_cnt
  # if curr_num == 0:
  #   ptr_at_zero += 1
  #   print(f'ptr+1 ==0')

print(f'PW: {ptr_at_zero}')