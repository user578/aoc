#!python

from pprint import pprint

filename = "eip1_1.txt"
filename = "eip1_2.txt"
filename = "eip1_3.txt"
filename = "eip1_4.txt"
filename = "eip1_5.txt"
filename = "input.txt"

a = []

# load from file
with open(filename) as file:
  for line in file:
    tmp = []
    for i in range(0, len(line)):
      if line[i] == '\n':
        continue
      else:
        if line[i] == '.':
          item = -1
        else:
          item = int(line[i])
        tmp.append(item)
    a.append(tmp)

pprint(a)


def walk(a, ci, cj, ends):
  print('+')
  print(f'{ci} {cj}')
  if a[ci][cj] == 9:
    print(f'walked to 9, p {ci} {cj}')
    ends.add((ci, cj))
    return ends
  # right
  if cj+1 < len(a[ci]) and a[ci][cj]+1 == a[ci][cj+1]:
    print(f'right {a[ci][cj+1]}, p {ci} {cj+1}')
    ends.union(walk(a, ci, cj+1, ends))
  # left
  if cj-1 >= 0 and a[ci][cj]+1 == a[ci][cj-1]:
    print(f'left {a[ci][cj-1]}, p {ci} {cj-1}')
    ends.union(walk(a, ci, cj-1, ends))
  # down
  if ci+1 < len(a) and a[ci][cj]+1 == a[ci+1][cj]:
    print(f'down {a[ci+1][cj]}, p {ci+1} {cj}')
    ends.union(walk(a, ci+1, cj, ends))
  # up
  if ci-1 >= 0 and a[ci][cj]+1 == a[ci-1][cj]:
    print(f'up {a[ci-1][cj]}, p {ci-1} {cj}')
    ends.union(walk(a, ci-1, cj, ends))
  print(f'No valid walk at {ci} {cj}')
  #exit(1)
  return ends

cnt_th = 0

for i in range(0, len(a)):
  for j in range(0, len(a[i])):
    if a[i][j] == 0:
      print(f'==== strart walk from 0, p {i} {j}')
      ends = set()
      ends = walk(a, i, j, ends)
      #pprint(f'ends: {ends}')
      cnt_th += len(ends)


print(cnt_th)
