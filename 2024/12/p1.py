#!python

from pprint import pprint

filename = "eip1_1.txt"
# filename = "eip1_2.txt"
# filename = "eip1_3.txt"
# filename = "eip1_4.txt"
# filename = "eip1_5.txt"
# filename = "input.txt"

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

# pprint(a)
# pprint(mask)


def is_plant_with_reg(a, ci, cj, plant, reg):
  #print(f'is_plant_with_reg({ci}, {cj}, {plant})')
  for ri in range(0, len(reg)):
    i = reg[ri][0]
    j = reg[ri][1]
    #print('-')
    if a[ci][cj] == plant and abs(i-ci+j-cj) == 1:
      #print('T')
      return True
  return False


def find_reg(a, ci, cj):
  plant = a[ci][cj]
  reg = []

  for i in range(ci, len(a)):
    for j in range(cj, len(a[i])):
      if (i == ci and j == cj) or is_plant_with_reg(a, i, j, plant, reg):
        reg.append([i,j])
        continue
  return reg


def reg_price(reg, a):
  fence = 0
  #print(f'is_plant_with_reg({ci}, {cj}, {plant})')
  for ri in range(0, len(reg)):
    neigh = 0
    for rj in range(0, len(reg)):
      if abs(reg[ri][0]-reg[rj][0]+reg[ri][1]-reg[rj][1]) == 1:
        neigh += 1
    fence += 4-neigh

  return fence * len(reg)


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


reg = find_reg(a, 0, 3)



# for i in range(0, len(a)):
#   for j in range(0, len(a[i])):
#     print(f'+{i} {j}')
#     if not is_plant_with_reg(a, i, j, a[i][j], found_r):
#       reg = find_reg(a, i, j)
#       print_reg(reg, a)
#       print(f'reg price: {reg_price(reg, a)}')
#       found_r += reg
