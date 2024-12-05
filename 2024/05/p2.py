#!python


from pprint import pprint

#filename = "ex_in.txt"
filename = "input.txt"

rules, updates = [], []
sum_mid_incorrect_fixed_upd = 0

# load from file
read_rules = True
with open(filename) as file:
  for line in file:
    if read_rules:
      if len(line) > 1:
        lst = [int(item.strip()) for item in line.split('|')]
        #print(lst)
        rules.append(lst)
      else:
        read_rules = False
        continue
    else:
      lst = [int(item.strip()) for item in line.split(',')]
      #print(lst)
      updates.append(lst)


def check_fix_item_for_rules(upd, i, before_list, rules):
  is_fixed = False

  for rule in rules:
    if upd[i] == rule[1] and \
       rule[0] not in before_list and \
       rule[0] in upd:
      print(f'Fail! Violates rule {rule} on item {upd[i]}')
      is_fixed = True
      if i < len(upd)-1:
        n = -1
        for k in range(0, len(upd)):
          if rule[0] == upd[k]:
            n = k
        print(f'But we fixed it {upd[i]} <-> {upd[n]}  ({i} <-> {n})')
        tmp = upd[i]
        upd[i] = upd[n]
        upd[n] = tmp
        print(upd)
      else:
        print(f'We can\'t fix it.')

  return is_fixed




for upd in updates:
  print(f'====')
  print(upd)
  is_fixed_update = False

  for i in range(0, len(upd)):
    while check_fix_item_for_rules(upd, i, upd[0:i], rules):
      is_fixed_update = True

  if not is_fixed_update:
    print(f'Good update!')
  if is_fixed_update:
    print(f'Fixed update!')
    mid_id = int((len(upd)-1)/2 + (len(upd)-1)%2)
    #print(mid_id)
    sum_mid_incorrect_fixed_upd += upd[mid_id]

print(f'====')
print(f'Sum: {sum_mid_incorrect_fixed_upd}')
