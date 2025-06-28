import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
electronics = list(map(int, input().split()))
multitap = []
order_list = []
cnt = 0

for index in range(len(electronics)):
  electronic = electronics[index]
  electronics[index] = -1
  if electronic in multitap:
    continue
  elif len(multitap) < n:
    multitap.append(electronic)
  else:
    latest_index = -1
    victim_index = -1
    for multitap_value in multitap:
      if multitap_value not in electronics:
        victim_index = multitap.index(multitap_value)
        break
      electronics_index = electronics.index(multitap_value)
      if electronics_index > latest_index:
        latest_index = electronics_index
    if victim_index == -1:
      victim_index = multitap.index(electronics[latest_index])
    multitap[victim_index] = electronic
    cnt += 1

print(cnt)