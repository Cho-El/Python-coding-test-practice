# 다익스트라
import sys
import heapq
from copy import deepcopy
INF = sys.maxsize
input = sys.stdin.readline
n,m,x = map(int, input().rstrip().split())
distance = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    graph[a].append((b,c))

def dijkstra(start):
    global distance
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

result = 0

distance = [INF] * (n + 1)
dijkstra(x)
distance1 = deepcopy(distance)

for i in range(1,n + 1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    result = max(result, distance[x] + distance1[i])

print(result)