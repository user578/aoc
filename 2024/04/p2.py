#!python

from pprint import pprint



#filename = "ex_in_p1.txt"
filename = "input.txt"

a = []
cnt = 0

def check_right_down(a, i, j):
  # check borders
  if j+1 <= len(a[i])-1 and i+1 <= len(a)-1:
    return a[i+1][j+1]
  else:
    return '_'

def check_left_down(a, i, j):
  # check borders
  if j-1 >= 0 and i+1 <= len(a)-1:
    return a[i+1][j-1]
  else:
    return '_'

def check_up_left(a, i, j):
  # check borders
  if i-1 >= 0 and j-1 >= 0:
    return a[i-1][j-1]
  else:
    return '_'

def check_up_right(a, i, j):
  # check borders
  if i-1 >= 0 and j+1 <= len(a[i])-1:
    return a[i-1][j+1]
  else:
    return '_'

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

# # print arr sizes
# print(len(a))
# for i in range(0, len(a)):
#   print(len(a[i]))

for i in range(0, len(a)):
  for j in range(0, len(a[i])):
    if a[i][j] == 'A':
      if ((check_right_down(a, i, j) == 'M' and
         check_up_left(a, i, j) == 'S') \
          or \
          (check_right_down(a, i, j) == 'S' and
         check_up_left(a, i, j) == 'M')) \
        \
        and \
        \
        ((check_up_right(a, i, j) == 'M' and
         check_left_down(a, i, j) == 'S') \
          or \
          (check_up_right(a, i, j) == 'S' and
         check_left_down(a, i, j) == 'M')):
         cnt += 1


print(cnt)