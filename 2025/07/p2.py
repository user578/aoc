#!python

from pprint import pprint


filename = "ex_in.txt"
filename = "input.txt"

a = []

# load line from file
from pathlib import Path
line = Path(filename).read_text()

# load lines from file
with open(filename) as file:
  for line in file:
    line = line.strip('\n')
    a.append(line)

#pprint(a)

# prepare timeline count map
cnt_tl_map = []
for i in range(0, len(a)):
  t = []
  for j in range(0, len(a[0])):
    t.append(0)
  cnt_tl_map.append(t)
# pprint(cnt_tl_map)
# exit(0)

def str_repl_ch_at_i(s, i, ch):
  return s[:i] + ch + s[i + 1:]

def print_timelines_over_beams(a, cnt_tl_map):
  for i in range(0, len(a)):
    for j in range(0, len(a[i])):
      if a[i][j] == '|':
        print(str(cnt_tl_map[i][j]).zfill(3), end='')
      else:
        print(f' {a[i][j]} ', end='')
    print()

# print_timelines_over_beams(a, cnt_tl_map)
# exit(0)

prev_line = a[0]
cnt_split = 0
for i, l in enumerate(a):
  if i == 0:
    prev_line = l
    continue
  # start beam line (1)
  if i == 1:
    for j in range(0, len(l)):
      if prev_line[j] == 'S':
        #print(j)
        l = str_repl_ch_at_i(l, j, '|')
        cnt_tl_map[i][j] += 1
  else: # other lines
    for j in range(0, len(l)):
      # beam falls to splitter
      if prev_line[j] == '|' and l[j] == '^':
        l = str_repl_ch_at_i(l, j-1, '|')
        cnt_tl_map[i][j-1] += cnt_tl_map[i-1][j]
        l = str_repl_ch_at_i(l, j+1, '|')
        cnt_tl_map[i][j+1] += cnt_tl_map[i-1][j]
        cnt_split += 1
        #print(f'Active splitter! {i},{j}')
      # beam falls down
      elif prev_line[j] == '|' and l[j] == '.':
        l = str_repl_ch_at_i(l, j, '|')
        cnt_tl_map[i][j] += cnt_tl_map[i-1][j]
        #print(f'Beam falls down! {i},{j}')
      elif prev_line[j] == '|' and l[j] == '|':
        l = str_repl_ch_at_i(l, j, '|')
        cnt_tl_map[i][j] += cnt_tl_map[i-1][j]
        #print(f'Beam falls down! {i},{j}')
  a[i] = l
  prev_line = l
  #pprint(a)
  #print_timelines_over_beams(a, cnt_tl_map)
  #input()

print(f'cnt_split={cnt_split}')
cnt_tl = 0
for j in range(0, len(cnt_tl_map[-1])):
  cnt_tl += cnt_tl_map[-1][j]
print(f'cnt_tl={cnt_tl}')