#!python

from pprint import pprint

filename = "eip2_1.txt"
# 80

filename = "eip2_2.txt"
# 436

filename = "eip2_3.txt"
# 236

filename = "eip2_4.txt"
# 368

filename = "eip2_5.txt"
# 1206

filename = "input.txt"

a = []
found_r = []

# load from file
with open(filename) as file:
  for line in file:
    tmp = []
    for i in range(0, len(line)):
      if line[i] == '\n':
        continue
      else:
        tmp.append(line[i])
    a.append(tmp)


def is_plant_add_to_reg(a, ci, cj, reg):
  plant = a[ci][cj]
  #print(f'is_plant_with_reg({ci}, {cj}, {plant})')
  is_to_add = False
  for ri in range(0, len(reg)):
    i = reg[ri][0]
    j = reg[ri][1]
    # print('+')
    # print(i, j, a[i][j])
    # print(ci, cj, a[ci][cj])
    if i == ci and j == cj:
      #print(f'duplicate plant {a[i][j]} {i} {j} in reg {reg}')
      return False # duplicate - already in reg
    #print('-')
    if a[ci][cj] == plant and \
       (i-ci == 0 or abs(i-ci) == 1) and \
       (j-cj == 0 or abs(j-cj) == 1) and \
       (abs(i-ci)+abs(j-cj) == 1 or abs(i-ci)+abs(j-cj) == 0):
      # print(f'ci,cj: {ci},{cj} with reg {reg}')
      # print(f'at cur i,j: {i},{j}')
      is_to_add = True

  if is_to_add:
    return True
  else:
    return False


def find_reg(a, ci, cj):
  plant = a[ci][cj]
  reg = [[ci,cj]]

  while True:
    is_found = False
    for i in range(ci, len(a)):
      for j in range(cj, len(a[i])):
        # input()
        # print(f'a[i][j]={a[i][j]}, {i}, {j}')
        if a[i][j] == plant and is_plant_add_to_reg(a, i, j, reg):
          is_found = True
          reg.append([i,j])
          continue
    # print('+')
    # print(f'reg: {reg}')
    # print(f'reg len: {len(reg)}')
    # input()
    for i in range(len(a)-1, -1, -1):
      for j in range(len(a[i])-1, -1, -1):
        if a[i][j] == plant and is_plant_add_to_reg(a, i, j, reg):
          is_found = True
          reg.append([i,j])
          continue
    if not is_found:
      break



  return reg


def is_inbounds(i,j,a):
  if not i < len(a) or \
      not i >= 0 or \
      not j < len(a[i]) or \
      not j >= 0:
    return False
  return True


def find_outer_neigh(a, si, sj, step_to_neigh, step_to_out):
  outer_neigh = []
  #print(f'{si} {sj}')
  # iterate over neighbors (starting from start tile)
  i = si - step_to_neigh[0]
  j = sj - step_to_neigh[1]
  while True:
    i += step_to_neigh[0]
    j += step_to_neigh[1]
    # print(f'+')
    # print(f'{i} {j}')
    # check neigh is in bounds
    if not is_inbounds(i,j,a):
      #print(f'neigh is not in bounds')
      return outer_neigh
    # check neigh is same plant
    if not a[si][sj] == a[i][j]:
      #print(f'neigh is not same plant')
      return outer_neigh
    # check neighbor is outer (check outer tile)
    io = i+step_to_out[0]
    jo = j+step_to_out[1]
    # check outer tile is in bounds
    if not is_inbounds(io,jo,a):
      #print(f'outer tile not not in bounds (found fence)')
      outer_neigh.append([i,j])
      continue
    # check outer tile is different plant
    if not a[i][j] == a[io][jo]:
      #print(f'outer tile is different plant (found fence)')
      outer_neigh.append([i,j])
      continue

    return outer_neigh


def is_coord_in_reg(i,j,reg):
  for n in range(0, len(reg)):
    if i == reg[n][0] and j == reg[n][1]:
      return True
  return False


def uniq_reg(reg):
  uniq = []
  for i in range(0, len(reg)):
    for j in range(0, len(reg)):
      if i == j or reg[i][0] != reg[j][0] and reg[i][1] != reg[j][1]:
        uniq.append(reg[i])
  return uniq


def reg_price(reg, a):
  reg_u_done, reg_d_done, reg_l_done, reg_r_done = [],[],[],[]
  fence = 0
  #print(reg)

  # iterate over reg
  for rn in range(0, len(reg)):
    #print('+')
    i = reg[rn][0]
    j = reg[rn][1]

    # find up fence
    if not is_coord_in_reg(i, j, reg_u_done):
      out_neigh = []
      out_neigh += find_outer_neigh(a, i, j, [0,1], [-1,0])
      out_neigh += find_outer_neigh(a, i, j, [0,-1], [-1,0])
      out_neigh = uniq_reg(out_neigh)
      reg_u_done += out_neigh
      if len(out_neigh) > 0:
        #print(f'found up fence: {out_neigh}, for: {reg[rn]}')
        fence += 1

    # find down fence
    if not is_coord_in_reg(i,j, reg_d_done):
      out_neigh = []
      out_neigh += find_outer_neigh(a, i, j, [0,1], [1,0])
      out_neigh += find_outer_neigh(a, i, j, [0,-1], [1,0])
      out_neigh = uniq_reg(out_neigh)
      reg_d_done += out_neigh
      if len(out_neigh) > 0:
        #print(f'found down fence: {out_neigh}, for: {reg[rn]}')
        fence += 1

    # find left fence
    if not is_coord_in_reg(i,j, reg_l_done):
      out_neigh = []
      out_neigh += find_outer_neigh(a, i, j, [1,0], [0,-1])
      out_neigh += find_outer_neigh(a, i, j, [-1,0], [0,-1])
      out_neigh = uniq_reg(out_neigh)
      reg_l_done += out_neigh
      if len(out_neigh) > 0:
        #print(f'found left fence: {out_neigh}, for: {reg[rn]}')
        fence += 1

    # find right fence
    if not is_coord_in_reg(i,j, reg_r_done):
      out_neigh = []
      out_neigh += find_outer_neigh(a, i, j, [1,0], [0,1])
      out_neigh += find_outer_neigh(a, i, j, [-1,0], [0,1])
      out_neigh = uniq_reg(out_neigh)
      reg_r_done += out_neigh
      if len(out_neigh) > 0:
        #print(f'found right fence: {out_neigh}, for: {reg[rn]}')
        fence += 1

  price = len(reg) * fence
  #print(f'{len(reg)}*{fence}={price}')
  return price


def print_reg(reg, a):
  for i in range(0, len(a)):
    for j in range(0, len(a[i])):
      found_in_reg = False
      for ri in range(0, len(reg)):
        if i == reg[ri][0] and j == reg[ri][1]:
          found_in_reg = True
          break
      if found_in_reg:
        print(a[i][j], end='')
      else:
        print('.', end='')
    print('')


def save_reg(reg, filepath):
  myfile = open(filepath, 'w')

  for i in range(0, len(a)):
    for j in range(0, len(a[i])):
      found_in_reg = False
      for ri in range(0, len(reg)):
        if i == reg[ri][0] and j == reg[ri][1]:
          found_in_reg = True
          break
      if found_in_reg:
        myfile.write(a[i][j])
      else:
        myfile.write('.')
    myfile.write('\n')

  myfile.close()


def is_plant_already_in_found_r(a, i, j, found_r):
  for ri in range(0, len(found_r)):
    if i == found_r[ri][0] and j == found_r[ri][1]:
      return True
  return False


#pprint(a)


# reg = find_reg(a, 0, 0)
# print_reg(reg, a)

t_price = 0

for i in range(0, len(a)):
  for j in range(0, len(a[i])):
    #print(f'+{i} {j}')
    if not is_plant_already_in_found_r(a, i, j, found_r):
      # print('+')
      # print(f'reg start: {a[i][j]}, {i}, {j}')

      reg = find_reg(a, i, j)
      #print_reg(reg, a)

      # n = 
      # print(n)
      # input()

      price = reg_price(reg, a)
      t_price += price
      found_r += reg

      # save_reg(reg, 'tmp.txt')
      # print(f'reg saved')

      #print(f'reg price: {price}')
      # input()

print(t_price)
