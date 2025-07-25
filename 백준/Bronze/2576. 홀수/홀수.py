import sys

num_list = [int(sys.stdin.readline()) for num in range(7)]
odd = False
odd_list = []

for num in num_list:
  if num%2 == 1:
    odd_list.append(num)
    odd = True

if odd == False:
  print(-1)
else:
  print(sum(odd_list))
  print(min(odd_list))