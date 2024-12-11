#!python

#!python

from pprint import pprint

filename = "ei_p1_1.txt"
filename = "ei_p1_2.txt"
filename = "input.txt"

a = []

# load from file
with open(filename) as file:
  for line in file:
    a = [int(item.strip()) for item in line.split(' ')]

print(a)


def split_int(i):
  while True:
    if i < 10:
      break



for i in range(0, len(a)):
  n = a[i]
  b = []
  for bl in range(0, 75):
    print(f'+ i={i} bl={bl+1}')
    cur_dig_len = len(str(n))

    # rule 1: If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if n == 0:
      b.append(1)
    # rule 2: If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    elif cur_dig_len % 2 == 0:
      b.append(int(str(n)[0:int(cur_dig_len/2)]))
      b.append(int(str(n)[int(cur_dig_len/2):]))
    # rule 3: If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    else:
      b.append(n*2024)

    # #print(b)
    # print(len(b))
    # tmp = a[0:len(a)]
    # a = b[0:len(b)]
    # b = []

print(f'len stones: {len(a)}')
