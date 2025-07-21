import sys

inf = 10000000000

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

edges = [[] for _ in range(n)]
visited = [False] * (n)
distance = [inf] * (n)

for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().rstrip().split())
  edges[a-1].append((b-1, c))

def get_shortest_node():
  min_distance = inf
  index = -1
  for i in range(n):
    if distance[i] < min_distance and not visited[i]:
      index = i
      min_distance =  distance[i]
  return index

def dijkstra(start):
  index = start-1
  distance[index] = 0

  for _ in range(n):
    index = get_shortest_node()
    if index == -1:
        break
    visited[index] = True
    for i in edges[index]:
      cost = distance[index] + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
  return (distance)

start, dest = map(int, sys.stdin.readline().rstrip().split())
print(dijkstra(start)[dest-1])