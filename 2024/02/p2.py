#!python

from pathlib import Path
from pprint import pprint

reports = []

def is_safe(rep, is_allow_to_remove_bad_level):
  # validate report len
  if len(rep) < 2:
    print(f'Report: {rep}')
    print('Error! Report must have at least 2 levels!')
    exit(1)

  # check if is increasing or decreasing
  if rep[1] > rep[0]:
    is_increasing = True
  elif rep[1] < rep[0]:
    is_increasing = False
  else:
    print(f'Unsafe! Nor increasing or decreasing at pos 1')
    if is_allow_to_remove_bad_level:
      print(f'Trying to del invalid lvl at pos 0')
      rep.pop(0)
      if is_safe(rep, False):
        print(f'Safe after del: {rep}')
        return True
    return False

  # iterate and check conditions
  for i in range(1, len(rep)):
    # increasing case
    if is_increasing:
      if rep[i] <= rep[i-1]:
        print(f'Unsafe! Stopped increasing at pos {i-1} ({rep[i-1]}): {rep}')
        if is_allow_to_remove_bad_level:
          return del_one_and_check_is_safe(rep)
        return False
      elif (rep[i]-rep[i-1]) > 3:
        print(f'Unsafe! Too high increase at pos {i-1} ({rep[i-1]}): {rep}')
        if is_allow_to_remove_bad_level:
          return del_one_and_check_is_safe(rep)
        return False
    # decreasing case
    else:
      if rep[i] >= rep[i-1]:
        print(f'Unsafe! Stopped decreasing at pos {i-1} ({rep[i-1]}): {rep}')
        if is_allow_to_remove_bad_level:
          return del_one_and_check_is_safe(rep)
        return False
      elif (rep[i-1]-rep[i]) > 3:
        print(f'Unsafe! Too high decreasing at pos {i-1} ({rep[i-1]}): {rep}')
        if is_allow_to_remove_bad_level:
          return del_one_and_check_is_safe(rep)
        return False

  print(f'Safe!')
  return True


def del_one_and_check_is_safe(rep_keep):
  for i in range(0, len(rep_keep)):
    # copy list obj
    rep=rep_keep[0:len(rep_keep)]
    rep.pop(i)
    if is_safe(rep, False):
      return True
  return False

#filename = "ex_in.txt"
filename = "input.txt"

reports_cnt, safe_cnt, unsafe_cnt = 0, 0, 0

# load from file
with open(filename) as f:
  for line in f:
    print('====')
    reports_cnt += 1
    rep_raw = line.split(' ')
    rep = [int(x.strip()) for x in rep_raw]

    if is_safe(rep, True):
      print(f'Report: {rep} is safe.')
      safe_cnt += 1
    else:
      print(f'Report: {rep} is unsafe.')
      unsafe_cnt += 1

print()
print(f'Safe+unsafe reports: {safe_cnt+unsafe_cnt}')
print(f'Total reports: {reports_cnt}')
print()
print(f'Safe reports: {safe_cnt}')
print(f'Unsafe reports: {unsafe_cnt}')

