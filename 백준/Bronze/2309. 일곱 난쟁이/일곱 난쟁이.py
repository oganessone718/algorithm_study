nanjangs = []

for _ in range(9):
    height, = map(int, input().split())
    nanjangs.append(height)

nanjangs.sort()

for i in range(9):
    for j in range(9):
        nanjang_i = nanjangs[i]
        nanjang_j = nanjangs[j]
        if sum(nanjangs)-nanjang_i-nanjang_j == 100:
            nanjangs.remove(nanjang_i)
            nanjangs.remove(nanjang_j)
            for nanjang in nanjangs:
                print(nanjang)
            exit()
