#!python

from pprint import pprint



#filename = "ex_in_p1.txt"
filename = "input.txt"

a = []
cnt = 0

def check_right(a, i, j):
  # check borders
  if j+3 > len(a[i])-1:
    return False
  if a[i][j+1] == 'M' and \
     a[i][j+2] == 'A' and \
     a[i][j+3] == 'S':
     return True
  return False

def check_down(a, i, j):
  # check borders
  if i+3 > len(a)-1:
    return False
  if a[i+1][j] == 'M' and \
     a[i+2][j] == 'A' and \
     a[i+3][j] == 'S':
     return True
  return False

def check_left(a, i, j):
  # check borders
  if j-3 < 0:
    return False
  if a[i][j-1] == 'M' and \
     a[i][j-2] == 'A' and \
     a[i][j-3] == 'S':
     return True
  return False

def check_up(a, i, j):
  # check borders
  if i-3 < 0:
    return False
  if a[i-1][j] == 'M' and \
     a[i-2][j] == 'A' and \
     a[i-3][j] == 'S':
     return True
  return False

def check_right_down(a, i, j):
  # check borders
  if j+3 > len(a[i])-1 or i+3 > len(a)-1:
    return False
  if a[i+1][j+1] == 'M' and \
     a[i+2][j+2] == 'A' and \
     a[i+3][j+3] == 'S':
     return True
  return False

def check_left_down(a, i, j):
  # check borders
  if j-3 < 0 or i+3 > len(a)-1:
    return False
  if a[i+1][j-1] == 'M' and \
     a[i+2][j-2] == 'A' and \
     a[i+3][j-3] == 'S':
     return True
  return False

def check_up_left(a, i, j):
  # check borders
  if i-3 < 0 or j-3 < 0:
    return False
  if a[i-1][j-1] == 'M' and \
     a[i-2][j-2] == 'A' and \
     a[i-3][j-3] == 'S':
     return True
  return False

def check_up_right(a, i, j):
  # check borders
  if i-3 < 0 or j+3 > len(a[i])-1:
    return False
  if a[i-1][j+1] == 'M' and \
     a[i-2][j+2] == 'A' and \
     a[i-3][j+3] == 'S':
     return True
  return False

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
    if a[i][j] == 'X':
      if check_right(a, i, j):
        cnt += 1
      if check_down(a, i, j):
        cnt += 1
      if check_left(a, i, j):
        cnt += 1
      if check_up(a, i, j):
        cnt += 1

      if check_right_down(a, i, j):
        cnt += 1
      if check_left_down(a, i, j):
        cnt += 1
      if check_up_left(a, i, j):
        cnt += 1
      if check_up_right(a, i, j):
        cnt += 1

print(cnt)