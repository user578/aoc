#!python

from pprint import pprint


def found_cheapest(a,b,p):
  for ai in range(0, 101):
    t = p[0:]
    for bi in range(0, 101):
      # print(f'=')
      # print(f'ai,bi:{ai},{bi}')
      sx = a[0]*ai+b[0]*bi
      sy = a[1]*ai+b[1]*bi
      # print(f'sx: {a[0]}*{ai}+{b[0]}*{bi}={sx}')
      # print(f'sy: {a[1]}*{ai}+{b[1]}*{bi}={sy}')
      # print(f'diff: {p[0]-sx}, {p[1]-sy}')
      if p[0]-sx < 0 or p[1]-sy < 0:
        break
      elif p[0]-sx == 0 and p[1]-sy == 0:
        # print(f'Found: ai,bi {ai},{bi}')
        return ai*3+bi*1

  return 0




filename = "ei_p1_1.txt"
filename = "input.txt"

sum = 0

# load from file
with open(filename) as file:
  cms = []
  cm = []
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
      p[0] = int(p[0].split(',')[0])
      p[1] = int(p[1].strip())
      cm.append(p)
      #print(p)
      continue
    else: # '\n'
      cms.append(cm)
      cm = []
      continue

#pprint(cms)



for cm in cms:
  pprint(cm)
  sum += found_cheapest(cm[0], cm[1], cm[2])

print(sum)