import sys
from collections import defaultdict
import heapq
INF = int(1e9)

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
start, end = map(int, sys.stdin.readline().rstrip().split())

dist = [INF] * (n+1)
prev_node = [0] * (n+1)

def dijkstra(start,end):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        weight, node = heapq.heappop(q)
        if dist[node] < weight:
            continue
        for adj_node, adj_weight in graph[node]:
            cost = weight + adj_weight
            if cost < dist[adj_node]:
                dist[adj_node] = cost
                prev_node[adj_node] = node
                heapq.heappush(q, (cost, adj_node))
    
    temp = dist[end]
    path = [str(end)]
    while prev_node[end]:
        end = prev_node[end]
        path.append(str(end))
    return '\n'.join((str(temp), str(len(path)), ' '.join(reversed(path))))
    
print(dijkstra(start,end))