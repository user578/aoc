#!python

from pprint import pprint


filename = "ex_in.txt"
filename = "input.txt"

banks = []

# load lines from file
with open(filename) as file:
  for line in file:
    banks.append(line.strip())

#pprint(banks)

def find_max_in_bank(bank):
  max = 0
  max_dir_lr = True
  max
  for i in range(1, 10):
    # x, drop_seq = drop_n_lowest(bank, i, True)
    # if x > max:
    #   max = x
    #   print(f'Found new max LR: {max}, drop_seq={drop_seq}')
    x, drop_seq = drop_n_lowest(bank, i, False)
    if x > max:
      max = x
      print(f'Found new max RL: {max}, drop_seq={drop_seq}')
  return max


def drop_n_lowest(bank, n_lowest, is_walk_direction_lr):
  drop_chars = ''
  drop_seq = ''
  drop_len = 0
  bank_len = len(bank)
  rest_bank = ''

  # prepare drop chars list
  for i in range(0, n_lowest+1):
    drop_chars += str(i)

  # prepare range numbers for walk
  if is_walk_direction_lr:
    start_ptr = 0
    end_ptr = bank_len
    step = 1
  else:
    start_ptr = bank_len-1
    end_ptr = -1
    step = -1

  #for ch in bank:
  # walk over string
  for i in range(start_ptr, end_ptr, step):
    if bank[i] in drop_chars and (bank_len - drop_len > 12):
      drop_len += 1
      if is_walk_direction_lr:
        drop_seq += bank[i]
      else:
        drop_seq = bank[i] + drop_seq
      continue
    else:
      if is_walk_direction_lr:
        rest_bank += bank[i]
      else:
        rest_bank = bank[i] + rest_bank

  rest_bank_len = len(rest_bank)

  # print('####')
  # print(f'drop_n_lowest(bank={bank}, n_lowest={n_lowest}, is_walk_direction_lr={is_walk_direction_lr})')
  # print(f'bank_len={bank_len}')
  # print(f'drop_chars={drop_chars}')
  # print(f'drop_seq={drop_seq}')
  # print(f'drop_len={drop_len}')
  # print(f'rest_bank={rest_bank}')
  # print(f'rest_bank_len={rest_bank_len}')

  # validate drop seq
  is_group_started = False
  for drop_char in drop_chars:
    if drop_char in drop_seq:
      is_group_started = True
    else:
      if is_group_started:
        #print(f'====INVALID DROP SEQ={drop_seq} : drop_char `{drop_char}` not in order of drop_seq!')
        return 0, ''

  if rest_bank_len == 12:
    return int(rest_bank), drop_seq
  else:
    return 0, ''


def find_max_subbank(bank, len_restriction_subbank):
  #print(f'####find_max_subbank(bank={bank}, len_restriction_subbank={len_restriction_subbank})')
  max = ''
  for n in range(9, 0, -1):
    for i, bat in enumerate(bank):
      #print(f'n={n} bat={bat} i={i}')
      if bat == str(n) and i+len_restriction_subbank<=len(bank):
        #print(f'Found in bank={bank} max_bat={bat}, i={i}')
        max += bat
        #print(f'max={max}')
        # if last, go forward
        if len_restriction_subbank == len(max):
          return max
        else:
          max += find_max_subbank(bank[i+1:], len_restriction_subbank-1)
          #print(f'max_n={max}')
          if len_restriction_subbank == len(max):
            return max

  return max


# tests v1
# max = find_max_in_bank('234234234234278')
# print(f'MAX={max}')
# drop_n_lowest('987654321111111', 3, False)

# run v1
# sum = 0
# for bank in banks:
#   max_in_bank = find_max_in_bank(bank)
#   print(f'{bank}  {max_in_bank}')
#   sum += max_in_bank

# print()
# print(f'SUM={sum}')


# tests v2
# max = find_max_subbank('818181911112111', 12)
# print(max)

# max = find_max_subbank('5453756862345874845337376263545357351615334758525567326257773648575775767585536364536457521766556466', 12)
# print(max)


# # run v2
sum = 0
for bank in banks:
  max_subbank = find_max_subbank(bank, 12)
  print(f'{bank}  {max_subbank}')
  sum += int(max_subbank)

print()
print(f'SUM={sum}')
