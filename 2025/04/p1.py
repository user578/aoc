#!python

from pprint import pprint


filename = "ex_in.txt"
filename = "input.txt"

a = []
ad = []

# load line from file
from pathlib import Path
line = Path(filename).read_text()

# load lines from file
with open(filename) as file:
  for line in file:
    row = []
    for i in range(0, len(line)):
      if line[i] == '\n':
        continue
      elif line[i] == '.':
        row.append(0)
      elif line[i] == '@':
        row.append(1)
      else:
        exit(1)
    a.append(row)

#pprint(a)

def count_rolls_around(a, i, j):
  coords_around = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
  ]
  cnt = 0
  for coord in coords_around:
    if i+coord[0] >= len(a) or \
       i+coord[0] < 0 or \
       j+coord[1] >= len(a[i]) or \
       j+coord[1] < 0:
      continue
    else:
      cnt += a[i+coord[0]][j+coord[1]]

  return cnt


# test
#print(count_rolls_around(a, 0, 2))

cnt_valid_rolls = 0

for i, row in enumerate(a):
  ad_row = []
  for j, place in enumerate(row):
    if a[i][j] == 0:
      ad_row.append('.')
    else:
      cnt_rolls = count_rolls_around(a, i, j)
      if cnt_rolls < 4:
        cnt_valid_rolls += 1
        ad_row.append('x')
      else:
        ad_row.append('@')
  ad.append(ad_row)

pprint(ad)
print(f'cnt_valid_rolls={cnt_valid_rolls}')