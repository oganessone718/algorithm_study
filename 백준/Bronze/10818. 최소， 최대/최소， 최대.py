n, = map(int, input().split())
origin_list = list(map(int, input().split()))

num = n

min = 1000001
max = -1000001
for i in origin_list:
    if min>i:
        min = i
    if max<i:
        max = i

print(min, max)