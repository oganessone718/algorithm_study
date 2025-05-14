people = 0
max = 0

for _ in range(10):
    n, m = map(int,input().split())
    people -= n
    people += m

    if max<people:
        max = people

print(max)
