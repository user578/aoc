#!python

#!python

from pprint import pprint

#filename = "ex_in.txt"
filename = "input.txt"


def change_str_item(str_, id_, item_):
  lst = list(str_)
  lst[id_] = item_
  str_ = ''.join(lst)

# 1=1
# 2=2
# 3=10
# 4=11
# 5=12
# 6=20
# 7=21
# 8=22
# 9=100

def int_to_ter(num):
  ter = [0]
  while num > 0:
    is_num_added = False
    #print(ter)
    i = len(ter)-1
    while not is_num_added:
      # print(f'====')
      # print(f'cur num: {num}')
      # print(f'cur ter: {ter}')
      # print(f'cur i: {i}')
      if i < 0:
        ter.insert(0, 1)
        num -= 1
        is_num_added = True
        continue
      if ter[i] == 0:
        ter[i] = 1
        num -= 1
        is_num_added = True
        continue
      elif ter[i] == 1:
        ter[i] = 2
        num -= 1
        is_num_added = True
        continue
      else: #ter[i] == '2'
        ter[i] = 0
        i -= 1
        continue

  return ''.join(str(x) for x in ter)


def get_ternary_signs_limit(eq):
  num_signs = len(eq)-1-1
  return 3**num_signs

def calculate(eq, ter_mask):
  vals = eq[1:]
  sum = eq[1]

  for i in range(1, len(vals)):
    if ter_mask[i-1] == '0':
      #print(f'{sum} + {vals[i]} = {sum + vals[i]}')
      sum = sum + vals[i]
    elif ter_mask[i-1] == '1':
      #print(f'{sum} * {vals[i]} = {sum + vals[i]}')
      sum = sum * vals[i]
    else:
      #print(f'{sum} || {vals[i]} = {sum + vals[i]}')
      sum = int(str(sum) + str(vals[i]))

  return sum


sum_total = 0
eqs = []

# load from file
with open(filename) as file:
  for line in file:
    eq = []
    eq.append(int(line.split(':')[0].strip()))
    vals_raw = line.split(':')[1].strip()
    #print(vals_raw)
    for x in vals_raw.split(' '):
      eq.append(int(x.strip()))
    eqs.append(eq)

# pprint(eqs)


# fill int_to_ter_map once
print('Calc itt map...')
itt = {}
#lim = get_ternary_signs_limit([183322025, 2, 8, 77, 5, 352, 8, 5, 7, 1, 2, 6, 5])
lim = get_ternary_signs_limit(eqs[4])
for i in range(0, lim):
  # print %
  #print(f'({i+1} of {lim})')
  for k in range(1, 11):
    if i == int(lim*(k/10)):
      print(f'{k*10}% ({i+1} of {lim})')
  # calc itt
  itt[i] = int_to_ter(i)
print('Done calc itt map.')

# calc
n = 0
for eq in eqs:
  ter_limit_str = int_to_ter(get_ternary_signs_limit(eq))
  ter_limit_int = get_ternary_signs_limit(eq)
  n += 1
  print(f'[{n}] {eq} len={len(eq)-1}')
  for i in range(0, ter_limit_int):
    # for k in range(1, 6):
    #   if k == int(i * k/20):
    #     print(f'{k*20}%')
    for k in range(1, 11):
      if i == int(ter_limit_int*(k/10)):
        print(f'{k*10}% ({i+1} of {ter_limit_int})')
    # calculate ternary mask
    ter_mask = itt[i].zfill(len(ter_limit_str)-1)
    #print(ter_mask)

    if eq[0] == calculate(eq, ter_mask):
      #print()
      sum_total += eq[0]
      break

print(sum_total)
