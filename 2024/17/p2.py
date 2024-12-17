#!python

#!python

from pprint import pprint




# filename = "ei_p2_1.txt"
filename = "input.txt"

r={}
p=[]
ptr = 0

# load from file
with open(filename) as file:
  cms = []
  cm = []
  for line in file:
    if 'Register A' in line:
      r['a'] = int(line.split(': ')[1])
      continue
    elif 'Register B' in line:
      r['b'] = int(line.split(': ')[1])
      continue
    elif 'Register C' in line:
      r['c'] = int(line.split(': ')[1])
      continue
    elif 'Program' in line:
      p_str = line.split(': ')[1]
      p = [int(item) for item in p_str.split(',')]
      continue
    else: # '\n'
      cms.append(cm)
      cm = []
      continue


def combo_operand(op,r):
  if op < 4:
    return op
  elif op == 4:
    return r['a']
  elif op == 5:
    return r['b']
  elif op == 6:
    return r['c']


def bitwise_xor(a, b):
  return a ^ b


def run(r,p,ptr):
  output = []
  while True:
    # print('====')
    opcode = p[ptr]
    op = p[ptr+1]

    if opcode == 0:
      result = int(r['a']/pow(2, combo_operand(op,r)))
      r['a'] = result
    elif opcode == 1:
      result = bitwise_xor(r['b'], op)
      r['b'] = result
    elif opcode == 2:
      result = combo_operand(op,r) % 8
      r['b'] = result
    elif opcode == 3:
      if r['a'] != 0:
        # print(f'a: {r["a"]}')
        # print(f'b: {r["b"]}')
        # print(f'c: {r["c"]}')
        # print(f'p: {p}')
        # print(f'ptr: {ptr}')
        # print(f'opcode: {opcode}')
        # print(f'op: {op}')
        # print('jnz')
        ptr = op
        continue
    elif opcode == 4:
      result = bitwise_xor(r['b'], r['c'])
      r['b'] = result
    elif opcode == 5:
      result = combo_operand(op,r) % 8
      output.append(result)
    elif opcode == 6:
      result = int(r['a']/pow(2, combo_operand(op,r)))
      r['b'] = result
    elif opcode == 7:
      result = int(r['a']/pow(2, combo_operand(op,r)))
      r['c'] = result

    # print(f'a: {r["a"]}')
    # print(f'b: {r["b"]}')
    # print(f'c: {r["c"]}')
    # print(f'p: {p}')
    # print(f'ptr: {ptr}')
    # print(f'opcode: {opcode}')
    # print(f'op: {op}')

    # continue steps
    ptr += 2
    if ptr > len(p)-1:
      return output

# print(bitwise_xor(1,1))
# exit(1)

def is_lists_eq(lst1, lst2):
  if len(lst1) != len(lst2):
    return False
  else:
    for i in range(0, len(lst1)):
      if lst1[i] != lst2[i]:
        return False
  return True

def is_last_x_items_eq(lst1, lst2, cnt):
  if len(lst1) != len(lst2):
    return False
  else:
    for i in range(len(lst1)-cnt, len(lst1)):
      if lst1[i] != lst2[i]:
        return False
  return True


# print(f'a: {r["a"]}')
# print(f'b: {r["b"]}')
# print(f'c: {r["c"]}')
# print(f'p: {p}')

# (!!!) Solved manually via increasing s and decreasing st:
s =  35000000000000
s = 164540892147389
e = 290000000000000
st=      1000000000
st=               1
for i in range(s, e, st):
  r["a"] = i
  output = run(r,p,ptr)

  print(i)


  if is_last_x_items_eq(p, output, 16):
    print(i)
    print(p)
    print(output)
    break


  # if is_lists_eq(p, output):
  #   print(f'a: {i}')
  #   print(output)
  #   break

  # print('====')
  # print('output: ', end='')
  # for i in range(0, len(output)):
  #   print(output[i], end='')
  #   if i != len(output)-1:
  #     print(',', end='')


# correct but not lowest:
#164545992421053
