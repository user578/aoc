#!python

from pprint import pprint


#filename = "ei_p2_t.txt"
#filename = "ei_p2_1.txt"
# ???

#filename = "ei_p2_2.txt"
# # 9021

filename = "input.txt"

f = []
moves = []
sum = 0

# load from file
with open(filename) as file:
  is_read_moves = False
  for line in file:
    tmp = []
    if line == '\n':
      is_read_moves = True
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
        if line[i] == '#':
          tmp.append('#')
          tmp.append('#')
        elif line[i] == 'O':
          tmp.append('[')
          tmp.append(']')
        elif line[i] == '.':
          tmp.append('.')
          tmp.append('.')
        elif line[i] == '@':
          tmp.append('@')
          tmp.append('.')
      f.append(tmp)


def get_box_move_last_coord(f,b,m):
  i,j = b[0],b[1]
  ni,nj = b[0]+m[0],b[1]+m[1]
  # print(f'st: {i},{j}')
  # print(f'st: {ni},{nj}')

  while True:
    # print(i,j)
    # print(ni,nj)
    if f[ni][nj] == '.':
      return [ni, nj]
    elif f[ni][nj] == '#':
      return []
    else: # in '[]'
      ni += m[0]
      nj += m[1]



def print_field(f):
  for i in range(0, len(f)):
    l = ''
    for j in range(0, len(f[i])):
      l += f[i][j]
    print(l)


def find_r(f):
  for i in range(0, len(f)):
    for j in range(0, len(f[i])):
      if f[i][j] == '@':
        return [i,j]
  return None


def walk_lr(f, m):
  r = find_r(f)
  # curr coords
  i = r[0]
  j = r[1]
  # next coords
  ni = r[0]
  nj = r[1]+m[1]

  # next move is '.'
  if f[ni][nj] == '.':
    f[i][j] = '.'
    f[ni][nj] = '@'
    return
  # next move is '#'
  elif f[ni][nj] == '#':
    return
  # next move in '[]'
  elif f[ni][nj] in '[]':
    c = get_box_move_last_coord(f, [ni,nj], m)
    if len(c) == 0:
      return

    # make move (move items in reverse order)
    # curr coords
    i = c[0]
    j = c[1]
    # next coords
    ni = c[0]
    nj = c[1]-m[1]
    while True:
      # print_field(f)
      # print(i,j)
      # print(ni,nj)
      # print()

      if f[ni][nj] == '@':
        f[i][j] = '@'
        f[ni][nj] = '.'
        # print_field(f)
        # print(i,j)
        # print(ni,nj)
        # print()
        return
      elif f[ni][nj] in '[]':
        f[i][j] = f[ni][nj]

      j  -= m[1]
      nj -= m[1]


def is_coords_in_lst(coords, lst):
  for i in range(0, len(lst)):
    if coords[0] == lst[i][0] and coords[1] == lst[i][1]:
      return True
  return False


def uniq_list_of_list_coords(lst):
  uniq = []
  for i in range(0, len(lst)):
    if not is_coords_in_lst(lst[i], uniq):
      uniq.append(lst[i])
  return uniq


def find_movable_box_stack(f, from_boxes, m):
  st = []
  is_must_move = False
  for ifb in range(0, len(from_boxes)):
    i = from_boxes[ifb][0]
    j = from_boxes[ifb][1]
    ni = i+m[0]
    nj = j+m[1]
    # print(i,j)
    # print(ni,nj)
    # print()
    if f[ni][nj] == ']':
      st.append([ni,nj])
      st.append([ni,nj-1])
      is_must_move = True
    elif f[ni][nj] == '[':
      st.append([ni,nj])
      st.append([ni,nj+1])
      is_must_move = True
    elif f[ni][nj] == '#':
      return False, []
    elif f[ni][nj] == '.':
      is_must_move = True

  st = uniq_list_of_list_coords(st)
  next_st = []
  for ist in range(0, len(st)):
    is_must_move, next_st = find_movable_box_stack(f, st, m)

  st = uniq_list_of_list_coords(st+next_st)

  return is_must_move, st


def walk_ud(f, m):
  r = find_r(f)
  # r curr coords
  i = r[0]
  j = r[1]
  # next coords
  ni = r[0]+m[0]
  nj = r[1]

  # next move is '.'
  if f[ni][nj] == '.':
    f[i][j] = '.'
    f[ni][nj] = '@'
    return
  # next move is '#'
  elif f[ni][nj] == '#':
    return
  # next move in '[]'
  elif f[ni][nj] in '[]':
    is_must_move, box_st = find_movable_box_stack(f, [[i,j]], m)

    # move boxes
    if is_must_move:
      for ib in range(len(box_st)-1, -1, -1):
        i,j = box_st[ib][0], box_st[ib][1]
        ni = i+m[0]
        nj = j+m[1]
        f[ni][nj] = f[i][j]
        f[i][j] = '.'
      f[r[0]+m[0]][r[1]+m[1]] = '@'
      f[r[0]][r[1]] = '.'

    # # curr coords
    # i = c[0]
    # j = c[1]
    # # next coords
    # ni = c[0]
    # nj = c[1]-m[1]
    # while True:
    #   # print_field(f)
    #   # print(i,j)
    #   # print(ni,nj)
    #   # print()

    #   if f[ni][nj] == '@':
    #     f[i][j] = '@'
    #     f[ni][nj] = '.'
    #     # print_field(f)
    #     # print(i,j)
    #     # print(ni,nj)
    #     # print()
    #     return
    #   elif f[ni][nj] in '[]':
    #     f[i][j] = f[ni][nj]

    #   j  -= m[1]
    #   nj -= m[1]






#print(moves)
print_field(f)
print('Start position')
print()

#print(find_movable_box_stack(f, [find_r(f)], [-1, 0]))


for i in range(0, len(moves)):
  if moves[i][0] == 1 or moves[i][0] == -1:
    walk_ud(f, moves[i])
  else:
    walk_lr(f, moves[i])
  # print_field(f)
  # print(f'move: {moves[i]}')
  # #input()
  # print()



for i in range(0, len(f)):
  for j in range(0, len(f[i])):
    if f[i][j] == '[':
      g = i*100+j
      sum += g
print(sum)