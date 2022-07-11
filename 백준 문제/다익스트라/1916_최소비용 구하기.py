# 다익스트라
import sys
import heapq
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    graph[a].append((b,c))

start, end = map(int, input().rstrip().split())

def dijkstra(start):
    distance = [float('inf')] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        
        for next_node in graph[node]:
            cost = dist + next_node[1]
            if distance[next_node[0]] > cost:
                distance[next_node[0]] = cost
                heapq.heappush(q, (cost, next_node[0]))
    
    return distance

result = dijkstra(start)
print(result[end])