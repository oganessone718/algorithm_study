input_num, = map(int, input().split())

fibo_list = [0,1,1]

def fibo(n):
    if n==1 and n==2:
        return 1
    if len(fibo_list)>n:
        return fibo_list[n]
    else:
        fibo_list.append(fibo(n-1)+fibo(n-2))
        return fibo_list[n]
    
print(fibo(input_num))