import sys
from itertools import combinations

n, k = map(int, sys.stdin.readline().rstrip().split())

k -= 5

if k < 0:
  print(0)
  sys.exit()

used_char_set = set()
essential_char_set = {'a', 'n', 't', 'i', 'c'}
word_list = []
for _ in range(n):
  word = set(sys.stdin.readline().rstrip())-essential_char_set
  if len(word) > k:
    continue
  word_list.append(word)
  used_char_set.update(word)

n = len(word_list)

if len(used_char_set) <= k:
  print(n)
  sys.exit()

char_combinations = combinations(used_char_set, k)

max_global = 0

for char_combination in char_combinations:
  char_combination_set = set(char_combination)
  max_local = 0
  for word in word_list:
    if (word <= char_combination_set):
      max_local+=1
  if max_local == n:
    print(n)
    sys.exit()
  if max_local > max_global:
    max_global = max_local

print(max_global)