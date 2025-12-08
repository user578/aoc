#!python

from pprint import pprint
import math

filename = "ex_in.txt"
filename = "input.txt"

a=[]
x=0
y=1
z=2
circuits=[]

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
    # elif (curr_dist < least_dist or least_dist < 0) and (not is_conn_in_conns([p, ap], conns)):
    #   closest_p = ap
    #   least_dist = curr_dist
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


cnt_conn = 0
while(True):
  print('---')
  p1,p2,cl_dist = find_two_closest_pts_in_arr(a)

  if cl_dist > 0:
    print(f'p1[x]*p2[x]={p1[x]*p2[x]}')

  if p1 is None or p2 is None:
    break

  connect_circ(p1,p2)
  #connect_conn(p1,p2)
  cnt_conn += 1
  print(f'cnt_conn={cnt_conn}')
  print(f'p1,p2: {p1},{p2}')
  print(f'cl_dist={cl_dist}')
  # print('circuits: ')
  # pprint(circuits)
  # print('conns: ')
  # pprint(conns)
  # print(f'circ len={len(circuits)}')

  # input()


print('====')
# print('circuits:')
# pprint(circuits)


# comment: не очень эффективно, отрабатывает ~30 минут
