a, b = map(int, input().split())

cnt = 0
num = 1
sum = 0

for i in range(1,1001):
    cnt+=1
    if a<=i<=b:
        sum+=num
    elif i>b:
        break
    if cnt == num:
        num += 1
        cnt = 0

print(sum)