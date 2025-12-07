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

pprint(a)

def str_repl_ch_at_i(s, i, ch):
  return s[:i] + ch + s[i + 1:]

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
        print(j)
        l = str_repl_ch_at_i(l, j, '|')
  else: # other lines
    for j in range(0, len(l)):
      # beam falls to splitter
      if prev_line[j] == '|' and l[j] == '^':
        l = str_repl_ch_at_i(l, j-1, '|')
        l = str_repl_ch_at_i(l, j+1, '|')
        cnt_split += 1
        print(f'Active splitter! {i},{j}')
      # beam falls down
      elif prev_line[j] == '|' and l[j] == '.':
        l = str_repl_ch_at_i(l, j, '|')
        #print(f'Beam falls down! {i},{j}')
  a[i] = l
  prev_line = l
  #pprint(a)
  #input()

print(f'cnt_split={cnt_split}')