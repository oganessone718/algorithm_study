import sys

h,w = map(int, sys.stdin.readline().rstrip().split())
block_list = list(map(int, sys.stdin.readline().rstrip().split()))
max_list = []

max = 0
for index in range(len(block_list)):
  max_list.append([max, block_list[index]])
  if max < block_list[index]:
    max = block_list[index]

block_list.reverse()
max = 0
for index in range(len(block_list)):
  max_list[len(block_list)-index-1].append(max)
  if max < block_list[index]:
    max = block_list[index]

total = 0
for max in max_list:
  if max[0]>max[1] and max[2]>max[1]:
    total += min(max[0],max[2])-max[1]

print(total)

