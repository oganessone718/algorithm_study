import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

degrees = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
queue = deque()
results = []

for line in range(m):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  graph[a].append(b)
  degrees[b]+=1

for index in range(1, len(degrees)):
  if degrees[index] == 0:
    queue.appendleft(index)

while len(queue) != 0:
  index_cur = queue.popleft()
  results.append(index_cur)
  for index_next in graph[index_cur]:
    degrees[index_next]-=1
    if degrees[index_next] == 0:
      queue.appendleft(index_next)

for result in results: 
  print(result, end=" ")
