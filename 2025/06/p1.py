#!python

from pprint import pprint


filename = "ex_in.txt"
filename = "input.txt"

arr = []
cnt_num_lines = 0

# load lines from file
is_num_line = True
with open(filename) as file:
  for il, line in enumerate(file):
    if line[0] == '*' or line[0] == '+':
      is_num_line = False
    else:
      cnt_num_lines += 1
    tmp_lst = line.split(' ')
    lst = []
    for l in tmp_lst:
      #print(f'[{l}]')
      l = l.strip('\n')
      if l != '' and l != '\n':
        if is_num_line:
          lst.append(int(l))
        else:
          lst.append(l)

    arr.append(lst)

#pprint(arr)
print(f'{len(arr[0])} == {len(arr[1])} == {len(arr[2])} == {len(arr[3])}')
print(cnt_num_lines)

def solve_problem(arr, i, cnt_num_lines):
  if arr[cnt_num_lines][i] == '*':
    res = 1
    for z in range(0, cnt_num_lines):
      res *= arr[z][i]
    return res
  else:
    res = 0
    for z in range(0, cnt_num_lines):
      res += arr[z][i]
    return res

sum = 0
for i in range(0, len(arr[0])):
  #print(f'{arr[0][i]} {arr[1][i]} {arr[2][i]}')
  sum += solve_problem(arr, i, cnt_num_lines)

print(sum)
