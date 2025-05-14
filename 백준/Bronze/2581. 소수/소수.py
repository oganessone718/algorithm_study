m, = map(int, input().split())
n, = map(int, input().split())

is_pri = True
primary = []

for i in range(m, n+1):
    if i==1:
        continue
    for j in range(2,i):
        if i%j == 0:
            is_pri = False
            break
    if is_pri is True:
        primary.append(i)
    is_pri = True

if(len(primary)==0):
    print(-1)
else:
    print(sum(primary))
    print(primary[0])