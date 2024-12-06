#!python

from pprint import pprint



#filename = "ex_in.txt"
filename = "input.txt"

a = []
direc = 3
# 0 - right
# 1 - down
# 2 - left
# 3 - up

g_pos = []

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

def chdirec(direc):
  if direc == 3:
    direc = 0
  else:
    direc += 1
  return direc


def move(g_pos, direc):
  i = g_pos[0]
  j = g_pos[1]

  if direc == 0:
    # right
    if j+1 > len(a[i])-1:
      return g_pos, direc, False
    if a[i][j+1] == '#':
      direc = chdirec(direc)
      print(f'Chdirec {direc} at {i}, {j}')
      return g_pos, direc, True
    else:
      a[i][j] = 'X'
      a[i][j+1] = '^'
      print(f'Move right at {i}, {j}')
      g_pos = [i, j+1]
      return g_pos, direc, True
    return g_pos, direc, False
  elif direc == 1:
    # down
    if i+1 > len(a)-1:
      return g_pos, direc, False
    if a[i+1][j] == '#':
      direc = chdirec(direc)
      print(f'Chdirec {direc} at {i}, {j}')
      return g_pos, direc, True
    else:
      a[i][j] = 'X'
      a[i+1][j] = '^'
      print(f'Move down at {i}, {j}')
      g_pos = [i+1, j]
      return g_pos, direc, True
  elif direc == 2:
    # left
    if j-1 < 0:
      return g_pos, direc, False
    if a[i][j-1] == '#':
      direc = chdirec(direc)
      print(f'Chdirec {direc} at {i}, {j}')
      return g_pos, direc, True
    else:
      a[i][j] = 'X'
      a[i][j-1] = '^'
      print(f'Move left at {i}, {j}')
      g_pos = [i, j-1]
      return g_pos, direc, True
    return g_pos, direc, False
  elif direc == 3:
    # up
    if i-1 < 0:
      return g_pos, direc, False
    if a[i-1][j] == '#':
      direc = chdirec(direc)
      print(f'Chdirec {direc} at {i}, {j}')
      return g_pos, direc, True
    else:
      a[i][j] = 'X'
      a[i-1][j] = '^'
      print(f'Move up at {i}, {j}')
      g_pos = [i-1, j]
      return g_pos, direc, True
    return g_pos, direc, False

#print(a)

for i in range(0, len(a)):
  for j in range(0, len(a[i])):
    if a[i][j] == '^':
      g_pos = [i, j]
      print(f'g_pos: {g_pos}')
      break

while True:
  g_pos, direc, is_moved = move(g_pos, direc)
  #pprint(a)
  #print(direc)
  #exit(1)

  if not is_moved:
    break

sum = 0
for i in range(0, len(a)):
  for j in range(0, len(a[i])):
    if a[i][j] == 'X':
      sum += 1

print(f'Sum (at): {sum+1}')