n, m = map(int, input().split())

gcd = 1
lcm = 1

for i in range(2,max(n,m)+1):
    cnt_n = 0
    cnt_m = 0
    while n % i == 0:
        n //= i
        cnt_n +=1
    while m % i == 0:
        m //= i
        cnt_m += 1
    gcd *= i ** min(cnt_n, cnt_m)
    lcm *= i ** max(cnt_n, cnt_m)

print(gcd)
print(lcm)