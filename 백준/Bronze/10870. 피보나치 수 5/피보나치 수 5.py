input_num, = map(int, input().split())

fibo_list = [0,1,1]

# 메모이제이션인데 굳이 재귀 안 써도... bottom up으로
# def fibo(n):
#     if len(fibo_list)>n:
#         return fibo_list[n]
#     else:
#         fibo_list.append(fibo(n-1)+fibo(n-2))
#         return fibo_list[n]

for _ in range(input_num-2):
    fibo_list.append(fibo_list[-1]+fibo_list[-2])

print(fibo_list[input_num])