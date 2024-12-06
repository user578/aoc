#!python

from pathlib import Path
from pprint import pprint

reports = []

def is_safe(rep):
  # validate report len
  if len(rep) < 2:
    print(f'Report: {rep}')
    print('Error! Report must have at least 2 rep!')
    exit(1)

  # check if is increasing or decreasing
  if rep[1] > rep[0]:
    is_increasing = True
  elif rep[1] < rep[0]:
    is_increasing = False
  else:
    print(f'Unsafe! Nor increasing or decreasing at pos 1')
    return False

  # iterate and check conditions
  for i in range(1, len(rep)):
    # increasing case
    if is_increasing:
      if rep[i] <= rep[i-1]:
        print(f'Unsafe! Stopped increasing at pos {i+1}')
        return False
      elif (rep[i]-rep[i-1]) > 3:
        print(f'Unsafe! Too high increase at pos {i+1}')
        return False
    # decreasing case
    else:
      if rep[i] >= rep[i-1]:
        print(f'Unsafe! Stopped decreasing at pos {i+1}')
        return False
      elif (rep[i-1]-rep[i]) > 3:
        print(f'Unsafe! Too high decreasing at pos {i+1}')
        return False

  print(f'Safe!')
  return True


#filename = "example_input.txt"
filename = "input.txt"

reports_cnt, safe_cnt, unsafe_cnt = 0, 0, 0

# load from file
with open(filename) as f:
  for line in f:
    reports_cnt += 1
    rep_raw = line.split(' ')
    rep = [int(x.strip()) for x in rep_raw]

    if is_safe(rep):
      print(f'Report: {rep} is safe.')
      safe_cnt += 1
    else:
      print(f'Report: {rep} is unsafe.')
      unsafe_cnt += 1

print(f'Safe reports: {safe_cnt}')
print(f'Unsafe reports: {unsafe_cnt}')
print(f'Safe+unsafe reports: {safe_cnt+unsafe_cnt}')
print(f'Total reports: {reports_cnt}')
