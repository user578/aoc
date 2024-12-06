#!python

from pathlib import Path
from pprint import pprint

#file_path = Path("ex_in.txt")
file_path = Path("input.txt")

a, b = [], []

# fill lists
with file_path.open("r") as file:
  for line in file:
    parts = line.split(maxsplit=1)
    a.append(int(parts[0].strip()))
    b.append(int(parts[1].strip()))

#print(f'Lists len: {len(a)}, {len(b)}')

sum = 0


for i in range(0, len(a)):
  cnt = 0
  for j in range(0, len(b)):
    if a[i] == b[j]:
      cnt += 1
  #print(a[i], cnt)
  sum += a[i] * cnt

print(f'sum: {sum}')
