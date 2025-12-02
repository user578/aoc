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
  #print(f'# CHECK={num}')
  if num < 10:
    return False

  s = str(num)
  l = len(s)
  l_2 = int(l/2)

  for seq_len in range(1, l_2+1):
    #print(f'seq_len={seq_len}')
    if l % seq_len != 0:
      continue
    first_seq = s[0:seq_len]
    #print(f'first_seq={first_seq}')
    is_all_seq_eq = True
    for i in range(1, int(l/seq_len)):
      next_seq=s[i*seq_len : i*seq_len+seq_len]
      #print(f'next_seq={next_seq}')
      if first_seq != next_seq:
        is_all_seq_eq = False
    if is_all_seq_eq:
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
  print(f'#### {r}')
  for num in range(r[0], r[1]+1):
    if is_num_invalid(num):
      sum += num
      print(f'INVALID_NUM={num}')
  print()

print(sum)
