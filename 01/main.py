#!python

from pathlib import Path
from pprint import pprint

file_path = Path("input.txt")

a, b = [], []

# fill lists
with file_path.open("r") as file:
  for line in file:
    parts = line.split(maxsplit=1)
    a.append(int(parts[0].strip()))
    b.append(int(parts[1].strip()))

a.sort()
b.sort()
print(f'Lists len: {len(a)}, {len(b)}')

dist = 0
for i in range(0, len(a)-1):
  dist += abs(a[i]-b[i])
  #print(f'{a[i]}  {b[i]}  {dist}')

print(f'Dist: {dist}')
