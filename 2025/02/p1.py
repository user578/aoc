#!python

from pprint import pprint


filename = "ex_in.txt"
filename = "input.txt"

a = []

# load from file
from pathlib import Path

line = Path(filename).read_text()

#pprint(line)

def is_ch_num(ch):
  if ch in '0123456789':
    return True
  return False


def is_num_invalid(num):
  s = str(num)
  l = len(s)
  l_2 = int(l/2)
  s1 = s[0:l_2]
  s2 = s[l_2:]
  #print(f'{s1} {s2}')
  if s1 == s2:
    return True
  return False


is_first_num = True
curr_num_ch = ''
curr_range = []

for i, ch in enumerate(line):
  if ch == '-':
    curr_range.append(int(curr_num_ch))
    is_first_num = False
    curr_num_ch = ''
    continue
  elif ch == ',' or i+1 == len(line):
    if i+1 == len(line):
      curr_num_ch += ch
    curr_range.append(int(curr_num_ch))
    a.append(curr_range)
    curr_range = []
    is_first_num = True
    curr_num_ch = ''
    continue
  else:
    curr_num_ch += ch

#pprint(a)

sum = 0

for r in a:
  print(r, end='')
  for num in range(r[0], r[1]+1):
    if is_num_invalid(num):
      sum += num
      print(f' {num}', end='')
  print()

print(sum)
