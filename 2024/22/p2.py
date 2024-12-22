#!python

from pprint import pprint
from collections import OrderedDict

# filename = "ei_p2_1.txt"
# filename = "ei_p2_2.txt"
filename = "input.txt"


init_secrets = []
sum = 0

# load from file
with open(filename) as file:
  for line in file:
    init_secrets.append(int(line.strip()))


#pprint(init_secrets)

def gen_next_secret(secret):
  # 1
  # x64, mix, prune
  secret = (secret ^ (secret*64)) % 16777216

  # 2
  # x/32, mix, prune
  secret = (secret ^ int(secret/32)) % 16777216

  # 3
  # x*2048, mix, prune
  secret = (secret ^ int(secret*2048)) % 16777216

  return secret


def gen_secret_iter(secret, iter, price_ch):
  prices = {}
  seq = tuple()
  prev_price = secret % 10
  for i in range(0, iter):
    #print(f'iter#: {i+1}')
    secret = gen_next_secret(secret)
    price = secret % 10
    ch = price - prev_price

    seq += (ch,)
    if len(seq) == 5:
      seq = seq[1:]

    if len(seq) == 4:
      if not seq in prices:
        prices[seq] = price
    #print(f'ch: {ch}, seq: {seq}, +{price}')
    #price_ch.append([price, ch])

    # actions before next iteration
    prev_price = price
  return prices


def save_list_to_file(lst, filepath):
  f = open(filepath,'w')
  f.write(str(lst))
  f.close()


def load_list_from_file(filepath):
  f = open(filepath,'r')
  data=f.read()
  f.close()
  return eval(data)


prices_ch = []
seq_prices = {}
for s in init_secrets:
  buyer_seq_prices = gen_secret_iter(s, 2000, prices_ch)
  # add to seq_prices dict
  for k,v in buyer_seq_prices.items():
    if k in seq_prices:
      seq_prices[k] += v
    else:
      seq_prices[k] = v

#save_list_to_file(prices_ch, './prices_ch.txt')
#prices_ch = load_list_from_file('./prices_ch.txt')
# print(len(prices_ch))

#print(profits)
max_price_seq = max(seq_prices, key=seq_prices.get)
max_price_val = seq_prices[max_price_seq]

print('seq_prices:')
for k,v in dict(sorted(seq_prices.items(), key=lambda item: item[1], reverse=True)).items():
  print(f'{k}: {v}')

print('==== RESULT ====')
print(max_price_seq)
print(max_price_val)
