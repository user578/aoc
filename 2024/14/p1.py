#!python

from pprint import pprint

# filename = "ei_p1.txt"
# # (!!!) filed size
# sizex = 11
# sizey = 7


filename = "input.txt"
# (!!!) filed size
sizex = 101
sizey = 103


rr = []
found_r = []

# load from file
with open(filename) as file:
  for line in file:
    t = line.split(' ')
    pos_str = t[0].split('=')[1]
    pos = [int(pos_str.split(',')[0].strip()), int(pos_str.split(',')[1].strip())]
    #print(pos)

    vel_str = t[1].split('=')[1]
    vel = [int(vel_str.split(',')[0].strip()), int(vel_str.split(',')[1].strip())]
    #print(vel)

    rr.append([pos, vel])

#pprint(r)


def print_field(sizex, sizey, rr, is_quadrants=False):
  f = []
  for y in range(0, sizey):
    ft = []
    for x in range(0, sizex):
      ft.append(0)
    f.append(ft)


  for y in range(0, sizey):
    for x in range(0, sizex):
      for r in rr:
        pos = r[0]
        posx = pos[0]
        posy = pos[1]
        if y == posy and x == posx:
          f[y][x] += 1

  vert_x = sizex//2 + sizex%2-1
  hor_y = sizey//2 + sizey%2-1

  for y in range(0, sizey):
    for x in range(0, sizex):
      if is_quadrants:
        if x == vert_x and y == hor_y:
          print('+', end='')
          continue
        elif x == vert_x:
          print('|', end='')
          continue
        elif y == hor_y:
          print('-', end='')
          continue
      if f[y][x] == 0:
        print('.', end='')
      else:
        print(f[y][x], end='')
    print('')



def walk(sizex, sizey, rr, sec):

  for r in rr:
    #print(f'curr r: {r}')
    pos = r[0]
    # print(f'pos: {pos}')
    posx = pos[0]
    posy = pos[1]
    vel = r[1]
    velx = vel[0]
    vely = vel[1]
    # print(f'({posx}+{velx*sec})%{sizex}')
    tposx = (posx+velx*sec)%sizex
    # print(f'({posy}+{vely*sec})%{sizey}')
    tposy = (posy+vely*sec)%sizey
    r[0] = [tposx, tposy]
    #print(tposx, tposy)


def calc_sf(sizex, sizey, rr):
  vert_x = sizex//2 + sizex%2-1
  hor_y = sizey//2 + sizey%2-1
  #print(vert_x, hor_y)

  q1,q2,q3,q4 = 0,0,0,0

  for r in rr:
    #print(f'curr r: {r}')
    pos = r[0]
    # print(f'pos: {pos}')
    posx = pos[0]
    posy = pos[1]

    if posx == vert_x or posy == hor_y:
      continue
    elif posx < vert_x and posy < hor_y:
      q1 += 1
    elif posx > vert_x and posy < hor_y:
      q2 += 1
    elif posx < vert_x and posy > hor_y:
      q3 += 1
    elif posx > vert_x and posy > hor_y:
      q4 += 1

  #print(f'qs: {q1},{q2},{q3},{q4}')
  return q1*q2*q3*q4



#rr = [rr[10]]

# print_field(sizex, sizey, rr)

walk(sizex, sizey, rr, 100)

# print()
# print_field(sizex, sizey, rr, True)


print(calc_sf(sizex, sizey, rr))
