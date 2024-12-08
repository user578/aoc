#!python

from pprint import pprint



#filename = "ex_in.txt"
#filename = "ex_in_p2.txt"
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
  anodes = []
  anodes.append([ist, jst])

  while True:
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
      anodes.append([ian, jan])
      ist = i
      jst = j
      i = ian
      j = jan
      continue
    else:
      break

    if ian == ist and jan == jst:
      break

  return anodes


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
        f_anodes = find_anode_loc(a, ist, jst, i, j)
        if len(f_anodes) > 0:
          print(f'Anodes found {f_anodes}')
          for an in f_anodes:
            if anodes[an[0]][an[1]] != '#':
              global cnt_an
              cnt_an += 1
              anodes[an[0]][an[1]] = '#'
              if a[an[0]][an[1]] == '.':
                a[an[0]][an[1]] = '#'

          # else:
          #   print(f'Placing an overlapping existing antenna {a[ian][jan]} at {ian} {jan}')

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
