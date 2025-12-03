#!python

from pprint import pprint


filename = "ex_in.txt"
filename = "input.txt"

arr = []

# load line from file
from pathlib import Path
line = Path(filename).read_text()

# load lines from file
with open(filename) as file:
  for line in file:
    for i in range(0, len(line)):
      if line[i] == '\n':
        continue
      elif line[i] == 'L':
        pass
      else:
        pass
    arr.append()

pprint(arr)
