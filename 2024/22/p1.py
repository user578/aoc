#!python

from pprint import pprint

# filename = "ei_p1_1.txt"
# filename = "ei_p1_2.txt"
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

def gen_secret_iter(secret, iter):
  for i in range(0, iter):
    secret = gen_next_secret(secret)
  return secret


for s in init_secrets:
  x = gen_secret_iter(s, 2000)
  print(x)
  sum += x

print('====')
print(sum)
