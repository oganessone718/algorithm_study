t, = map(int, input().split())

for i in range(t):
    n, = map(int, input().split())
    max_exp = 0
    answer = ""
    while True:
        if n<2**(max_exp+1):
            break
        max_exp+=1
    for j in range(max_exp,-1,-1):
        if n>=2**j:
            n= n%(2**j)
            answer = str(j) + " " + answer
    print(answer)