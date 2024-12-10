#!python

from pprint import pprint

filename = "eip2_1.txt"
filename = "eip2_2.txt"
filename = "eip2_3.txt"
filename = "eip2_4.txt"
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


def walk(a, ci, cj, ends, r):
  print('+')
  print(f'{ci} {cj}')
  if a[ci][cj] == 9:
    print(f'walked to 9, p {ci} {cj}')
    ends.add((ci, cj))
    r += 1
    return r, ends
  # right
  if cj+1 < len(a[ci]) and a[ci][cj]+1 == a[ci][cj+1]:
    print(f'right {a[ci][cj+1]}, p {ci} {cj+1}')
    r, e = walk(a, ci, cj+1, ends, r)
    ends.union(e)
  # left
  if cj-1 >= 0 and a[ci][cj]+1 == a[ci][cj-1]:
    print(f'left {a[ci][cj-1]}, p {ci} {cj-1}')
    r, e = walk(a, ci, cj-1, ends, r)
    ends.union(e)
  # down
  if ci+1 < len(a) and a[ci][cj]+1 == a[ci+1][cj]:
    print(f'down {a[ci+1][cj]}, p {ci+1} {cj}')
    r, e = walk(a, ci+1, cj, ends, r)
    ends.union(e)
  # up
  if ci-1 >= 0 and a[ci][cj]+1 == a[ci-1][cj]:
    print(f'up {a[ci-1][cj]}, p {ci-1} {cj}')
    r, e = walk(a, ci-1, cj, ends, r)
    ends.union(e)
  print(f'No valid walk at {ci} {cj}')
  #exit(1)
  return r, ends

cnt_th = 0
total_r = 0

for i in range(0, len(a)):
  for j in range(0, len(a[i])):
    if a[i][j] == 0:
      print(f'==== strart walk from 0, p {i} {j}')
      ends = set()
      r = 0
      r, ends = walk(a, i, j, ends, r)
      #pprint(f'ends: {ends}')
      print(f'r: {r}')
      total_r += r
      cnt_th += len(ends)

print(f'total_r: {total_r}')
