#!python

#!python

from pprint import pprint


def get_input():
  #filename = "ex_in.txt"
  filename = "input.txt"

  a = []
  # load from file
  with open(filename) as file:
    for line in file:
      arr = []
      for i in range(0, len(line)):
        if line[i] == '\n':
          continue
        else:
          arr.append(line[i])
      a.append(arr)

  return a


def chdirec(direc):
  if direc == 3:
    direc = 0
  else:
    direc += 1
  return direc


def move(a, g_pos, direc):
  i = g_pos[0]
  j = g_pos[1]
  chdirec_id = []

  if direc == 0:
    # right
    if j+1 > len(a[i])-1:
      return g_pos, direc, chdirec_id, False
    if a[i][j+1] == '#':
      chdirec_id = [i, j+1, direc]
      direc = chdirec(direc)
      print(f'Chdirec {direc} at {i}, {j}')
      return g_pos, direc, chdirec_id, True
    else:
      a[i][j] = 'X'
      a[i][j+1] = '^'
      print(f'Move right at {i}, {j}')
      g_pos = [i, j+1]
      return g_pos, direc, chdirec_id, True
    return g_pos, direc, chdirec_id, False
  elif direc == 1:
    # down
    if i+1 > len(a)-1:
      return g_pos, direc, chdirec_id, False
    if a[i+1][j] == '#':
      chdirec_id = [i+1, j, direc]
      direc = chdirec(direc)
      print(f'Chdirec {direc} at {i}, {j}')
      return g_pos, direc, chdirec_id, True
    else:
      a[i][j] = 'X'
      a[i+1][j] = '^'
      print(f'Move down at {i}, {j}')
      g_pos = [i+1, j]
      return g_pos, direc, chdirec_id, True
  elif direc == 2:
    # left
    if j-1 < 0:
      return g_pos, direc, chdirec_id, False
    if a[i][j-1] == '#':
      chdirec_id = [i, j-1, direc]
      direc = chdirec(direc)
      print(f'Chdirec {direc} at {i}, {j}')
      return g_pos, direc, chdirec_id, True
    else:
      a[i][j] = 'X'
      a[i][j-1] = '^'
      print(f'Move left at {i}, {j}')
      g_pos = [i, j-1]
      return g_pos, direc, chdirec_id, True
    return g_pos, direc, chdirec_id, False
  elif direc == 3:
    # up
    if i-1 < 0:
      return g_pos, direc, chdirec_id, False
    if a[i-1][j] == '#':
      chdirec_id = [i-1, j, direc]
      direc = chdirec(direc)
      print(f'Chdirec {direc} at {i}, {j}')
      return g_pos, direc, chdirec_id, True
    else:
      a[i][j] = 'X'
      a[i-1][j] = '^'
      print(f'Move up at {i}, {j}')
      g_pos = [i-1, j]
      return g_pos, direc, chdirec_id, True
    return g_pos, direc, chdirec_id, False



def check_obs_stuck(chdirec_ids, chdirec_id):
  for ci in chdirec_ids:
    if ci[0] == chdirec_id[0] and \
       ci[1] == chdirec_id[1] and \
       ci[2] == chdirec_id[2]:
       return True
  return False



def check_stuck(a):
  direc = 3
  # 0 - right
  # 1 - down
  # 2 - left
  # 3 - up

  g_pos = []
  cnt_stuck_obs = 0
  chdirec_ids = []

  for i in range(0, len(a)):
    for j in range(0, len(a[i])):
      if a[i][j] == '^':
        g_pos = [i, j]
        print(f'g_pos: {g_pos}')
        break

  moves = 0
  while True:
    g_pos, direc, chdirec_id, is_moved = move(a, g_pos, direc)

    if is_moved:
      moves += 1
      if len(chdirec_id):
        if not check_obs_stuck(chdirec_ids, chdirec_id):
          chdirec_ids.append(chdirec_id)
        else:
          #print(f'STUCKED!!!')
          return True
    else:
      #print(f'NOT STUCKED!!!')
      return False


cnt_stuck_obs = 0
a = get_input()

for i in range(0, len(a)):
  for j in range(0, len(a[i])):
    print(f'Curr id [z]: {i},{j}')
    if a[i][j] == '^' or a[i][j] == '#':
      continue
    else:
      new_a = get_input()
      new_a[i][j] = '#'
      if check_stuck(new_a):
        cnt_stuck_obs += 1

print(f'Cnt: {cnt_stuck_obs}')

# sum = 0
# for i in range(0, len(a)):
#   for j in range(0, len(a[i])):
#     if a[i][j] == 'X':
#       sum += 1
# print(f'Sum (at): {sum+1}')
