n, = map(int, input().split())
m = list(map(int, input().split()))

cnt = 0

for number in m:
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
            break
    
    if is_prime and number != 1:
        cnt += 1
    
print(cnt)