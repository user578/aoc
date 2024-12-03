#!python

sum = 0
numbers = '0123456789'

# define vars
num1, num2 = 0, 0
curr_num = ''
is_disable_muls = False

curr_mul_str = ''
mul_stg = 0
# 0 - m
# 1 - u
# 2 - l
# 3 - (
# 4 - first number or ,
# 5 - second number or )

curr_do_str = ''
do_stg = 0
# 0 - d
# 1 - o
# 2 - (
# 3 - )

curr_dont_str = ''
dont_stg = 0
# 0 - none
# 1 - '
# 2 - t
# 3 - (
# 4 - )

#filename = "ex_in_p2.txt"
filename = "input.txt"

reports_cnt, safe_cnt, unsafe_cnt = 0, 0, 0

# load from file
with open(filename) as f:
  for a in f:
    for i in range(0, len(a)):
      # mul_stg 0 - m
      if mul_stg == 0:
        if a[i] == 'm':
          curr_mul_str = 'm'
          mul_stg += 1
          continue
        else:
          #print(f'Bad mul: {curr_mul_str+a[i]}')
          mul_stg = 0
          #continue
      # mul_stg 1 - u
      if mul_stg == 1:
        if a[i] == 'u':
          curr_mul_str += a[i]
          mul_stg += 1
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          mul_stg = 0
          continue
      # mul_stg 2 - l
      if mul_stg == 2:
        if a[i] == 'l':
          curr_mul_str += a[i]
          mul_stg += 1
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          mul_stg = 0
          continue
      # mul_stg 3 - (
      if mul_stg == 3:
        if a[i] == '(':
          mul_stg += 1
          curr_mul_str += a[i]
          curr_num = ''
          num1, num2 = 0, 0
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          mul_stg = 0
          continue
      # mul_stg 4 - first number or ,
      if mul_stg == 4:
        if a[i] in numbers:
          curr_num = curr_num + a[i]
          if len(curr_num) > 3:
            print(f'Bad mul: {curr_mul_str+a[i]}')
            mul_stg = 0
            continue
          else:
            curr_mul_str += a[i]
            continue
        elif a[i] == ',':
          # num 1 is found + next mul_stg
          num1 = int(curr_num)
          curr_num = ''
          curr_mul_str += a[i]
          mul_stg += 1
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          mul_stg = 0
          continue

      # mul_stg 5 - second number or )
      if mul_stg == 5:
        if a[i] in numbers:
          curr_num = curr_num + a[i]
          if len(curr_num) > 3:
            print(f'Bad mul: {curr_mul_str+a[i]}')
            mul_stg = 0
            continue
          else:
            curr_mul_str += a[i]
            continue
        elif a[i] == ')':
          # num 2 is found + next mul_stg
          curr_mul_str += a[i]
          num2 = int(curr_num)
          mul = num1 * num2
          if not is_disable_muls:
            sum += mul
          print(f'Found correct mul at pos {i+1}: {num1}*{num2} = {mul}')
          print(f'Found mul: {curr_mul_str}')
          print(f'Current sum: {sum}')
          curr_mul_str = ''
          num1, num2 = 0, 0
          curr_num = ''
          mul_stg = 0
          continue
        else:
          print(f'Bad mul: {curr_mul_str+a[i]}')
          mul_stg = 0
          continue


      # do stages
      # 0 - d
      # 1 - o
      # 2 - (   # or transit to don't
      # 3 - )

      # do_stg 0 - d
      if do_stg == 0:
        if a[i] == 'd':
          curr_do_str = a[i]
          do_stg += 1
          continue
        else:
          #print(f'Bad do: {curr_do_str+a[i]}')
          do_stg = 0
          #continue
      if do_stg == 1:
        if a[i] == 'o':
          curr_do_str += a[i]
          do_stg += 1
          continue
        else:
          print(f'Bad do: {curr_do_str+a[i]}')
          do_stg = 0
          continue
      if do_stg == 2:
        if a[i] == '(':
          curr_do_str += a[i]
          do_stg += 1
          continue
        # transit to `don't` stg
        elif a[i] == 'n':
          curr_dont_str = curr_do_str + a[i]
          curr_do_str = ''
          do_stg = 0
          dont_stg = 1
          continue
        else:
          print(f'Bad do: {curr_do_str+a[i]}')
          do_stg = 0
          continue
      if do_stg == 3:
        if a[i] == ')':
          curr_do_str += a[i]
          do_stg = 0
          is_disable_muls = False
          print(f'Found correct do at pos {i+1}')
          continue
        else:
          print(f'Bad do: {curr_do_str+a[i]}')
          do_stg = 0
          continue


        # don't stages
        # 0 - none
        # 1 - '
        # 2 - t
        # 3 - (
        # 4 - )
      if dont_stg == 1:
        if a[i] == "'":
          curr_dont_str += a[i]
          dont_stg += 1
          continue
        else:
          print(f'Bad dont: {curr_dont_str+a[i]}')
          dont_stg = 0
          continue
      if dont_stg == 2:
        if a[i] == 't':
          curr_dont_str += a[i]
          dont_stg += 1
          continue
        else:
          print(f'Bad dont: {curr_dont_str+a[i]}')
          dont_stg = 0
          continue
      if dont_stg == 3:
        if a[i] == '(':
          curr_dont_str += a[i]
          dont_stg += 1
          continue
        else:
          print(f'Bad dont: {curr_dont_str+a[i]}')
          dont_stg = 0
          continue
      if dont_stg == 4:
        if a[i] == ')':
          dont_stg = 0
          is_disable_muls = True
          print(f'Found correct dont at pos {i+1}')
          curr_dont_str = ''
          continue
        else:
          print(f'Bad dont: {curr_dont_str+a[i]}')
          dont_stg = 0
          continue


print(f'sum: {sum}')
