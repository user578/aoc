#!python

from pprint import pprint

filename = "ei_p2_1.txt"
#filename = "ei_p2_2.txt"
filename = "input.txt"

a = []
sum = 0

# load from file
with open(filename) as file:
  for line in file:
    a = [int(item.strip()) for item in line.split(' ')]

#print(a)


def calc(a, total_steps, cur_step):
  print('====')
  print(f'START cur_step={cur_step}')
  #print(f'a before step: {a}')
  if cur_step == total_steps+1:
    print(f'Exit OVERFLOW step {cur_step}')
    return len(a)
  l = 0
  i = 0
  # iterate over list
  while True:
    print(f'+ Loop step: {cur_step} at i: {i}')
    print(f'a: {a}')
    expanded = []
    cur_dig_len = len(str(a[i]))
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

    l += calc(expanded, total_steps, cur_step+1)
    print(f'-- returned to step: {cur_step}, i: {i}')
    print(f'a[i]: {a[i]}, a: {a}')
    print(f'l: {l}')

    if i+1 == len(a):
      print(f'Exit STEP {cur_step} at i: {i} of {len(a)}')
      print(f'a: {a}')
      print(f'l: {l}')
      break
    else:
      i += 1

  return len(a)



a = [0, 0]
sum = calc(a, 3, 1)

print(f'tot len stones: {sum}')
