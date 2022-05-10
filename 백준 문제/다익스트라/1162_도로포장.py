import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline
n,m,k = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for info in graph[node]:
            cost = dist + info[0]
            if cost < distance[info[1]]:
                distance[info[1]] = cost
                heapq.heappush(q, info)
        