#!python

from pprint import pprint


filename = "ex_in.txt"
filename = "input.txt"

arr = []
cnt_num_lines = 0

# load lines from file
is_num_line = True
with open(filename) as file:
  for line in file:
    line = line.strip('\n')
    if line[0] != '*' and line[0] != '+':
      cnt_num_lines += 1
    arr.append(line)

#pprint(arr)
for l in arr:
  print(f'{l}    [{len(l)}]')
print()


def get_sign(arr, i, cnt_num_lines, old_sign):
  if arr[cnt_num_lines][i] == '*' or arr[cnt_num_lines][i] == '+':
    return arr[cnt_num_lines][i], True
  else:
    return old_sign, False


def get_num(arr, i, cnt_num_lines):
  num = ''
  for c in range(0, cnt_num_lines):
    if arr[c][i] != ' ':
      num += arr[c][i]
  if len(num) > 0:
    return int(num)
  else:
    return None


def calc_gr_res(gr, sign):
  if len(gr) == 0:
    return 0
  elif sign == '+':
    res = 0
    for i in range(0, len(gr)):
      res += int(gr[i])
    return res
  else: #'*'
    res = 1
    for i in range(0, len(gr)):
      res *= int(gr[i])
    return res

print()
print(f'====')
curr_sign = ''
prev_sign = ''
curr_gr = []
sum = 0
for i in range(0, len(arr[0])):
  prev_sign = curr_sign
  curr_sign, is_sign_changed = get_sign(arr, i, cnt_num_lines, curr_sign)
  if is_sign_changed:
    add_res = calc_gr_res(curr_gr, prev_sign)
    sum += add_res
    curr_gr = []
    print(f'res: {add_res}')
    print('---')

  num = get_num(arr, i, cnt_num_lines)
  if num is None:
    continue
  else:
    curr_gr.append(num)
    print(f'{num} {curr_sign}')

  # last el
  if i == len(arr[0])-1:
    add_res = calc_gr_res(curr_gr, prev_sign)
    sum += add_res
    curr_gr = []
    print(f'res: {add_res}')
    print('---')

print(f'SUM={sum}')