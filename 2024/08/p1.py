#!python

from pprint import pprint



#filename = "ex_in.txt"
filename = "input.txt"

a = []
anodes = []
cnt_an = 0

# load from file
with open(filename) as file:
  for line in file:
    arr = []
    for i in range(0, len(line)):
      if line[i] == '\n':
        continue
      else:
        arr.append(line[i])
    a.append(arr)

with open(filename) as file:
  for line in file:
    arr = []
    for i in range(0, len(line)):
      if line[i] == '\n':
        continue
      else:
        arr.append(line[i])
    anodes.append(arr)

# 1 8 - 2 5
# 3 2
def find_anode_loc(a, ist, jst, i, j):
  ian, jan = -1, -1
  is_found = False

  if i > ist:
    ian = i + (i-ist)
  elif i < ist:
    ian = i - (ist-i)
  else:
    ian = ist

  if j > jst:
    jan = j + (j-jst)
  elif j < jst:
    jan = j - (jst-j)
  else:
    ian = ist

  if ian < len(a) and jan < len(a[0]) and \
     ian >= 0 and jan >= 0:
     is_found = True

  if ian == ist and jan == jst:
      is_found = False

  return is_found, ian, jan


def find_and_place_antinodes(a, ist, jst, ch):
  print('====')
  print(f'Finding antinodes for {ch}, pos {ist} {jst}')

  # find all antinodes
  for i in range(0, len(a)):
    for j in range(0, len(a[i])):
      if i == ist and jst == j:
        continue
      if a[i][j] == ch:
        print('+')
        print(f'Found same antenna {ch} at {i} {j}')
        is_found, ian, jan = find_anode_loc(a, ist, jst, i, j)
        if is_found:
          print(f'Anode found at {ian} {jan}')
          if anodes[ian][jan] != '#':
            global cnt_an
            cnt_an += 1
            anodes[ian][jan] = '#'
          if a[ian][jan] == '.':
            a[ian][jan] = '#'

          else:
            print(f'Placeing an overlapping existing antenna {a[ian][jan]} at {ian} {jan}')

pprint(a)

for i in range(0, len(a)):
  for j in range(0, len(a[i])):
    if a[i][j] == '.':
      continue
    elif a[i][j] == '#':
      continue
    else:
      find_and_place_antinodes(a, i, j, a[i][j])
      # pprint(a)
      # exit(1)

pprint(a)
print(cnt_an)
