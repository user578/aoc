#!python

from pprint import pprint


# def found_cheapest(a,b,p):
#   for ai in range(0, 10000000000):
#     t = p[0:]
#     for bi in range(10000000000, -1, -1):
#       # print(f'iter={(ai+1)*(bi+1)}')
#       print(f'=')
#       print(f'ai,bi:{ai},{bi}')
#       sx = a[0]*ai+b[0]*bi
#       sy = a[1]*ai+b[1]*bi
#       print(f'sx: {a[0]}*{ai}+{b[0]}*{bi}={sx}')
#       print(f'sy: {a[1]}*{ai}+{b[1]}*{bi}={sy}')
#       print(f'diff: {p[0]-sx}, {p[1]-sy}')
#       if p[0]-sx < 0 or p[1]-sy < 0:
#         break
#       elif p[0]-sx == 0 and p[1]-sy == 0:
#         print(f'Found: ai,bi {ai},{bi}')
#         return ai*3+bi*1

#   return 0


filename = "ei_p2_1.txt"
filename = "ei_p2_2.txt"
filename = "input.txt"


def found_cheapest(c):
  a0=c[0][0]
  a1=c[0][1]
  b0=c[1][0]
  b1=c[1][1]
  p0=c[2][0]
  p1=c[2][1]

  print(f'====')

  print(f'a0={a0}')
  print(f'a1={a1}')
  print(f'b0={b0}')
  print(f'b1={b1}')
  print(f'p0={p0}')
  print(f'p1={p1}')

  up, down = (p0*b1-p1*b0), (a0*b1-b0*a1)
  if up%down != 0:
    return 0
  ai = up/down
  print(f'ai: {ai}')
  bi=(p1-a1*ai)/b1
  print(f'bi: {bi}')

  return ai*3+bi*1





sum = 0

# load from file
with open(filename) as file:
  cms = []
  cm  = []
  for line in file:
    if 'Button A' in line:
      a = line.split('+')[1:]
      a[0] = int(a[0].split(',')[0])
      a[1] = int(a[1].strip())
      cm.append(a)
      #print(a)
      continue
    elif 'Button B' in line:
      b = line.split('+')[1:]
      b[0] = int(b[0].split(',')[0])
      b[1] = int(b[1].strip())
      cm.append(b)
      #print(b)
      continue
    elif 'Prize' in line:
      p = line.split('=')[1:]
      p[0] = int(p[0].split(',')[0])+10000000000000
      p[1] = int(p[1].strip())+10000000000000
      cm.append(p)
      #print(p)
      continue
    else: # '\n'
      cms.append(cm)
      cm = []
      continue

#pprint(cms)



for cm in cms:
  price = found_cheapest(cm)
  sum += price
  print(f'price: {price}')

print(sum)
