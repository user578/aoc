#!python


from pprint import pprint

#filename = "ex_in.txt"
filename = "input.txt"

rules, updates = [], []
sum_mid_correct_upd = 0

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


def check_item_for_rules(item, before_list, rules, update):
  # is_in_first_rule = False
  # for rule in rules:
  #   if item == rule[0]:
  #     is_in_first_rule = True
  #     break

  # if not is_in_first_rule:
  #   print(f'Fail! Not in first rule!')
  #   return False

  for rule in rules:
    if item == rule[1] and \
       rule[0] not in before_list and \
       rule[0] in update:
      print(f'Fail! Violates rule {rule} on item {item}')
      return False

  return True




for upd in updates:
  print(f'==== {upd}')
  is_valid_update = True

  for i in range(0, len(upd)):
    if not check_item_for_rules(upd[i], upd[0:i], rules, upd):
      print(f'Bad update!')
      is_valid_update = False
      break

  if is_valid_update:
    print(f'Good update!')
    mid_id = int((len(upd)-1)/2 + (len(upd)-1)%2)
    #print(mid_id)
    sum_mid_correct_upd += upd[mid_id]

print(f'====')
print(f'Sum: {sum_mid_correct_upd}')
