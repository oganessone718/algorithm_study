import sys

n,s = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

left = 0
right = 0
length = 100001
sum_num = num_list[0]

while right < n:
  if sum_num >= s:
    if length > right - left + 1 :
      length = right - left + 1
    if length == 1 :
      print(length)
      exit()
    else:
      sum_num -= num_list[left]
      left += 1
  elif sum_num < s:
    right += 1
    if right == n:
      break
    sum_num += num_list[right]
    
if length == 100001:
  print(0)
else:
  print(length)