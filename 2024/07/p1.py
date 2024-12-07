#!python

from pprint import pprint

#filename = "ex_in.txt"
filename = "input.txt"


def bin_to_str(b):
  return str(b)[2:]

def get_binary_signs_limit(eq):
  num_signs = len(eq)-1-1
  return 2**num_signs

def calculate(eq, bin_mask):
  vals = eq[1:]
  sum = eq[1]

  for i in range(1, len(vals)):
    if bin_mask[i-1] == '0':
      #print(f'{sum} + {vals[i]} = {sum + vals[i]}')
      sum = sum + vals[i]
    else:
      #print(f'{sum} * {vals[i]} = {sum + vals[i]}')
      sum = sum * vals[i]

  return sum


sum_total = 0
eqs = []

# load from file
with open(filename) as file:
  for line in file:
    eq = []
    eq.append(int(line.split(':')[0].strip()))
    vals_raw = line.split(':')[1].strip()
    #print(vals_raw)
    for x in vals_raw.split(' '):
      eq.append(int(x.strip()))
    eqs.append(eq)

pprint(eqs)


for eq in eqs:
  for i in range(0, get_binary_signs_limit(eq)):
    # calculate binary mask
    bin_mask = bin_to_str(bin(i)).zfill(len(bin_to_str(bin(get_binary_signs_limit(eq))))-1)
    #print(bin_mask)

    if eq[0] == calculate(eq, bin_mask):
      print()
      sum_total += eq[0]
      break

print(sum_total)
