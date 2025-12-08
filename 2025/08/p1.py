#!python

from pprint import pprint
import math

# filename = "ex_in.txt"
# cnt_conn_lim = 10

filename = "input.txt"
cnt_conn_lim = 1000


a=[]
x=0
y=1
z=2
circuits=[]
conns = []

# load line from file
from pathlib import Path
line = Path(filename).read_text()

# load lines from file
with open(filename) as file:
  for line in file:
    tmp_lst = line.split(',')
    lst = []
    for item in tmp_lst:
      lst.append(int(item.strip('\n')))
    a.append(lst)


#pprint(a)
def is_p1_p2_eq(p1, p2):
  if p1[x]==p2[x] and p1[y]==p2[y] and p1[z]==p2[z]:
    return True
  return False


def calc_dist(p1, p2):
  return math.sqrt((p2[x]-p1[x])**2 + (p2[y]-p1[y])**2 + (p2[z]-p1[z])**2)


# def is_connected(p1, p2, m):
#   if p1 in m:
#     if p2 in m[p1]:
#       return True
#   if p2 in m:
#     if p1 in m[p2]:
#       return True
#   return False


def is_p1_p2_in_the_same_circ(p1,p2,circuits):
  c1_id = find_circuit_id_of_p(p1,circuits)
  if c1_id < 0:
    return False
  c2_id = find_circuit_id_of_p(p2,circuits)
  if c1_id == c2_id:
    return True
  return False


def find_closest_of_p_in_arr(p, a):
  closest_p = None
  least_dist = -1

  for ap in a:
    if is_p1_p2_eq(p, ap):
      continue
    curr_dist = calc_dist(p, ap)
    if (curr_dist < least_dist or least_dist < 0) and (not is_p1_p2_in_the_same_circ(p, ap, circuits)):
      closest_p = ap
      least_dist = curr_dist
    elif (curr_dist < least_dist or least_dist < 0) and (not is_conn_in_conns([p, ap], conns)):
      closest_p = ap
      least_dist = curr_dist
  return closest_p


def find_two_closest_pts_in_arr(a):
  cl_dist = -1
  p1,p2 = None,None
  for ap in a:
    #print(f'ap={ap}')
    curr_closest_p = find_closest_of_p_in_arr(ap, a)
    if curr_closest_p is None:
      continue
    curr_closest_p_dist = calc_dist(ap, curr_closest_p)
    if curr_closest_p_dist < cl_dist or cl_dist < 0:
      cl_dist = curr_closest_p_dist
      p1,p2 = ap,curr_closest_p
  #print(p1,p2)
  return p1,p2,cl_dist


def find_circuit_id_of_p(p, circuits):
  for i, circuit in enumerate(circuits):
    for cp in circuit:
      if is_p1_p2_eq(p, cp):
        return i
  return -1

def is_p_in_circ(p, circuit):
  for cp in circuit:
    if is_p1_p2_eq(p, cp):
      return True
  return False

def connect_circ(p1, p2):
  c1_id = find_circuit_id_of_p(p1,circuits)
  c2_id = find_circuit_id_of_p(p2,circuits)
  # connect p1-p2
  if c1_id < 0 and c2_id < 0:
    circuits.append([p1, p2])
  # connect p1-c2
  elif c1_id < 0 and c2_id >= 0:
    circuits[c2_id].append(p1)
  # connect p2-c1
  elif c2_id < 0 and c1_id >= 0:
    circuits[c1_id].append(p2)
  # connect c1-c2
  elif c1_id >= 0 and c2_id >= 0 and c1_id != c2_id:
    circuits[c1_id] = circuits[c1_id] + circuits[c2_id]
    circuits.pop(c2_id)


def is_conn_in_conns(c1, conns):
  for conn in conns:
    if c1[0][x] == conn[0][x] and \
       c1[0][y] == conn[0][y] and \
       c1[0][z] == conn[0][z] and \
       c1[1][x] == conn[1][x] and \
       c1[1][y] == conn[1][y] and \
       c1[1][z] == conn[1][z]:
      return True
    elif c1[1][x] == conn[0][x] and \
         c1[1][y] == conn[0][y] and \
         c1[1][z] == conn[0][z] and \
         c1[0][x] == conn[1][x] and \
         c1[0][y] == conn[1][y] and \
         c1[0][z] == conn[1][z]:
      return True
  return False


def connect_conn(p1, p2):
  if not is_conn_in_conns([p1,p2], conns):
    conns.append([p1,p2])

# print(calc_dist([162, 817, 812], [425, 690, 689]))
# print(calc_dist([162, 817, 812], [431,825,988]))
# #print(find_closest_of_p_in_arr(a[0], a))

# print(find_two_closest_pts_in_arr(a))
# # #a.pop(0)
# a.pop(-1)
# # pprint(a)

# circuits = [
#   [[1,1,1],[2,2,2]],
#   [[3,3,3],[4,4,4]]
# ]
# connect([1,1,1], [3,3,3])
# pprint(circuits)

# print(is_p1_p2_in_the_same_circ([1,1,1], [2,2,2]))
# pprint(circuits)



# circuits = [[[162, 817, 812], [425, 690, 689], [431, 825, 988]]]
# conns = [[[162, 817, 812], [425, 690, 689]], [[162, 817, 812], [431, 825, 988]]]
# a = [[162, 817, 812],[431, 825, 988]]
# print(find_two_closest_pts_in_arr(a))

def find_max_in_lst(lst):
  max = -1
  for itm in lst:
    if itm > max:
      max = itm
  return max


def get_new_lst_removing_val(val, lst):
  new_lst = []
  for i in range(0, len(lst)):
    if lst[i] != val:
      new_lst.append(lst[i])
  return new_lst


def find_three_largest_nums(lst):
  maxes = []
  # max 1
  max1 = find_max_in_lst(lst)
  maxes.append(max1)
  lst = get_new_lst_removing_val(max1, lst)
  # max 2
  max2 = find_max_in_lst(lst)
  maxes.append(max2)
  lst = get_new_lst_removing_val(max2, lst)
  # max 3
  max3 = find_max_in_lst(lst)
  maxes.append(max3)
  lst = get_new_lst_removing_val(max3, lst)

  return maxes

cnt_conn = 0
while(True):
  print('---')
  p1,p2,cl_dist = find_two_closest_pts_in_arr(a)

  if p1 is None or p2 is None:
    break

  connect_circ(p1,p2)
  connect_conn(p1,p2)
  cnt_conn += 1
  print(f'cnt_conn={cnt_conn}')
  # print(f'p1,p2,cl_dist: {p1},{p2},{cl_dist}')
  # print('circuits: ')
  # pprint(circuits)
  # print('conns: ')
  # pprint(conns)

  if cnt_conn == cnt_conn_lim:
    break
  #input()


print('====')
print('circuits:')
pprint(circuits)

circ_szs = []
for c in circuits:
  circ_szs.append(len(c))
print('circ_szs:')
pprint(circ_szs)

maxes = find_three_largest_nums(circ_szs)
print('maxes:')
print(maxes)

mult_largest_circ_sizes = 1*maxes[0]*maxes[1]*maxes[2]
print('mult_largest_circ_sizes: ', mult_largest_circ_sizes)

# comment: не очень эффективно, отрабатывает ~10-15 минут
