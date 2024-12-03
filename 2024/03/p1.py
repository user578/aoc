#!python

sum = 0
numbers = '0123456789'

# define vars
num1, num2 = 0, 0
curr_num = ''
curr_mul_str = ''
stage = 0
# 0 - m
# 1 - u
# 2 - l
# 3 - (
# 4 - first number or ,
# 5 - second number or )


# filename = "ex_in_p1.txt"
filename = "input.txt"

reports_cnt, safe_cnt, unsafe_cnt = 0, 0, 0

# load from file
with open(filename) as f:
  for a in f:
    for i in range(0, len(a)):
      # stage 0 - m
      if stage == 0:
        if a[i] == 'm':
          curr_mul_str = 'm'
          stage += 1
          continue
        else:
          #print(f'Bad mul: {curr_mul_str+a[i]}')
          stage = 0
          continue
      # stage 1 - u
      if stage == 1:
        if a[i] == 'u':
          curr_mul_str += a[i]
          stage += 1
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          stage = 0
          continue
      # stage 2 - l
      if stage == 2:
        if a[i] == 'l':
          curr_mul_str += a[i]
          stage += 1
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          stage = 0
          continue
      # stage 3 - (
      if stage == 3:
        if a[i] == '(':
          stage += 1
          curr_mul_str += a[i]
          curr_num = ''
          num1, num2 = 0, 0
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          stage = 0
          continue
      # stage 4 - first number or ,
      if stage == 4:
        if a[i] in numbers:
          curr_num = curr_num + a[i]
          if len(curr_num) > 3:
            print(f'Bad mul: {curr_mul_str+a[i]}')
            stage = 0
            continue
          else:
            curr_mul_str += a[i]
            continue
        elif a[i] == ',':
          # num 1 is found + next stage
          num1 = int(curr_num)
          curr_num = ''
          curr_mul_str += a[i]
          stage += 1
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          stage = 0
          continue

      # stage 5 - second number or )
      if stage == 5:
        if a[i] in numbers:
          curr_num = curr_num + a[i]
          if len(curr_num) > 3:
            print(f'Bad mul: {curr_mul_str+a[i]}')
            stage = 0
            continue
          else:
            curr_mul_str += a[i]
            continue
        elif a[i] == ')':
          # num 2 is found + next stage
          curr_mul_str += a[i]
          num2 = int(curr_num)
          mul = num1 * num2
          sum += mul
          print(f'Found correct mul at pos {i+1}: {num1}*{num2} = {mul}')
          print(f'Found mul: {curr_mul_str}')
          print(f'Current sum: {sum}')
          curr_mul_str = ''
          num1, num2 = 0, 0
          curr_num = ''
          stage = 0
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          stage = 0
          continue


print(f'sum: {sum}')
