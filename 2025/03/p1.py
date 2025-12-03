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

def find_highest_jol_ch(bank):
  for ch in '9876543210':
    for i, bat in enumerate(bank):
      if bat == ch:
        # skip last digit
        if i == len(bank)-1:
          continue
        return ch, i+1

def find_lowest_jol_ch(bank, start_ptr):
  for ch in '9876543210':
    for i in range(start_ptr, len(bank)):
      if bank[i] == ch:
        return ch

sum = 0
for bank in banks:
  highest_jol_ch, start_ptr = find_highest_jol_ch(bank)
  lowest_jol_ch = find_lowest_jol_ch(bank, start_ptr)
  print(f'{bank}  {highest_jol_ch}{lowest_jol_ch}')
  sum += int(highest_jol_ch+lowest_jol_ch)

print(sum)