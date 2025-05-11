n, m = map(int, input().split())

cnt = 0
answer = 0

for i in range(n):
    if n%(i+1) == 0:
        cnt+=1
        if cnt == m:
            answer = i+1
            break

print(answer)