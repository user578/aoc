#!python

from pprint import pprint

# filename = "ei1.txt"
# filename = "ei2.txt"
filename = "input.txt"

a = []
sum = 0

m = {}

# load from file
with open(filename) as file:
  for line in file:
    a = [int(item.strip()) for item in line.split(' ')]

#print(a)


def calc(a, total_steps, cur_step, is_use_maps=False):
  # print('====')
  # print(f'START cur_step={cur_step}')
  l = 0
  i = 0
  # iterate over list
  for i in range(0, len(a)):
    if cur_step <= 10 and is_use_maps:
      print(f'{cur_step}, {i+1}/{len(a)}')
    # print(f'+ Start loop step: {cur_step} at i: {i}')
    # print(f'a: {a}')
    expanded = []
    cur_dig_len = len(str(a[i]))
    # use MAP
    if is_use_maps and a[i] < 100 and total_steps-cur_step < 35:
      l += m[a[i]][total_steps-cur_step+1]
      continue
    # rule 1: If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if a[i] == 0:
      expanded.append(1)
    # rule 2: If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    elif cur_dig_len % 2 == 0:
      expanded.append(int(str(a[i])[0:int(cur_dig_len/2)]))
      expanded.append(int(str(a[i])[int(cur_dig_len/2):]))
    # rule 3: If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    else:
      expanded.append(a[i]*2024)

    if cur_step == total_steps:
      # print(f'Exit OVERFLOW step {cur_step}')
      # print(f'a: {expanded}')
      l += len(expanded)
      continue
    else:
      l += calc(expanded, total_steps, cur_step+1, is_use_maps)
      # print(f'-- returned to step: {cur_step}, i: {i}')
      # print(f'a[i]: {a[i]}, a: {a}')
      # print(f'l: {l}')

  return l


def save_dict_to_file(d, filepath):
  f = open(filepath,'w')
  f.write(str(d))
  f.close()

def load_dict_from_file(filepath):
  f = open(filepath,'r')
  data=f.read()
  f.close()
  return eval(data)

#a = [22, 22]
# 0: 0
# 1: 1
# 2: 2024
# 3: 20 24

# First, calc this and save dicts to files:

# for i in range(0, 100):
#   print(i)
#   tm = {}
#   for j in range(1, 36):
#     tm[j] = calc([i], j, 1)
#   #m[i] = tm
#   save_dict_to_file(tm, f'./m/{i}.txt')

# Then load dicts from files for speed up calculations:
for i in range(0, 100):
  print(i)
  m[i] = load_dict_from_file(f'./m/{i}.txt')

#a = [0, 0]
sum = calc(a, 75, 1, True)

print(f'tot len stones: {sum}')
