#!python

from pprint import pprint

#filename = "eip1_1.txt"
# 140

filename = "eip1_2.txt"
# 772

filename = "eip1_3.txt"
# 1930

filename = "eip1_4.txt"


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


def reg_price(reg, a):
  fence = 0
  #print(reg)
  for ri in range(0, len(reg)):
    #print('+')
    neigh = 0
    for rj in range(0, len(reg)):
      if (reg[ri][0]-reg[rj][0] == 0 or abs(reg[ri][0]-reg[rj][0]) == 1) and \
         (reg[ri][1]-reg[rj][1] == 0 or abs(reg[ri][1]-reg[rj][1]) == 1) and \
         ( abs(reg[ri][0] - reg[rj][0]) + abs(reg[ri][1] - reg[rj][1]) == 1):
        # print(f'item: {reg[ri][0]} {reg[ri][1]}')
        # print(f'neigh: {reg[rj][0]} {reg[rj][1]}')
        neigh += 1
    fence += 4-neigh
    # print(f'cur fence: {4-neigh}')

  price = fence * len(reg)
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
      price = reg_price(reg, a)
      t_price += price
      found_r += reg

      #print_reg(reg, a)

      # save_reg(reg, 'tmp.txt')
      # print(f'reg saved')

      # print(f'reg price: {price}')
      # input()

print(t_price)
