#!python

from pprint import pprint

filename = "ei_p1_1.txt"
# 2028

filename = "ei_p1_2.txt"
# 10092

filename = "input.txt"

f = []
moves = []
sum = 0

# load from file
with open(filename) as file:
  is_read_moves = False
  il = 0
  for line in file:
    tmp = []
    if line == '\n':
      is_read_moves = True
      il += 1
      continue
    # read moves
    if is_read_moves:
      for i in range(0, len(line)):
        #print(line[i], end='')
        if line[i] == '>':
          moves.append([0,1])
        elif line[i] == 'v':
          moves.append([1,0])
        elif line[i] == '<':
          moves.append([0,-1])
        elif line[i] == '^':
          moves.append([-1,0])
        else:
          moves.append([0,0])
    # read field
    else:
      for i in range(0, len(line)):
        if line[i] == '\n':
          continue
        if line[i] == '@':
          r = [il,i]
          tmp.append('.')
          continue
        tmp.append(line[i])

      f.append(tmp)

    il += 1


# pprint(f)
# pprint(moves)
# pprint(r)

def get_box_move_coords(f,box,m):
  i,j = box[0],box[1]
  ni,nj = box[0]+m[0],box[1]+m[1]
  # print(f'st: {i},{j}')
  # print(f'st: {ni},{nj}')

  while True:
    # print(i,j)
    # print(ni,nj)
    if f[ni][nj] == '.':
      return [ni, nj]
    elif f[ni][nj] == '#':
      return []
    else: # == 'O'
      ni += m[0]
      nj += m[1]


def walk(f,r,m):
  # next move is '.'
  i = r[0]
  j = r[1]
  ni = r[0]+m[0]
  nj = r[1]+m[1]
  if f[ni][nj] == '.':
    f[i][j] = '.'
    r = [ni, nj]
    return r
  # next move is '#'
  elif f[ni][nj] == '#':
    return r
  # next move is 'O'
  elif f[ni][nj] == 'O':
    c = get_box_move_coords(f, [ni,nj], m)
    if len(c) > 0:
      f[c[0]][c[1]] = 'O'
      f[ni][nj] = '.'
      r = [ni, nj]
      return r
    else:
      return r

def print_field(f, r):
  for i in range(0, len(f)):
    l = ''
    for j in range(0, len(f[i])):
      if i == r[0] and j == r[1]:
        l += '@'
      else:
        l += f[i][j]
    print(l)


# print_field(f, r)
# print()

for i in range(0, len(moves)):
  r = walk(f,r,moves[i])
  #print_field(f, r)
  #print(f'move: {moves[i]}')
  #input()
  #print()



for i in range(0, len(f)):
  for j in range(0, len(f[i])):
    if f[i][j] == 'O':
      g = i*100+j
      sum += g
print(sum)