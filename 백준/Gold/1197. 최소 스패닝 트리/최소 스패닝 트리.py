import sys

sys.setrecursionlimit(10**6)

def find_root(roots, node):
  if roots[node] != node:
    roots[node] = find_root(roots, roots[node])
  return roots[node]

def union (roots,a,b):
  root_a = find_root(roots, a)
  root_b = find_root(roots, b)

  if root_a < root_b:
    roots[root_b] = root_a
  else:
    roots[root_a] = root_b


v,e = map(int, sys.stdin.readline().rstrip().split())

edges = []
for _ in range(e):
  a,b,c = map(int, sys.stdin.readline().rstrip().split())
  edges.append((c,a,b))
edges.sort()

roots = [i for i in range(v+1)]

weight = 0

for edge in edges:
  c,a,b = edge
  if find_root(roots, a) != find_root(roots,b):
    union(roots,a,b)
    weight += c

print(weight)