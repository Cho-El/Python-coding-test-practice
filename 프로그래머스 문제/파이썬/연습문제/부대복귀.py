import heapq
import sys
from collections import defaultdict

INF = sys.maxsize
def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    for road in roads:
        start, end = road
        graph[start].append((end,1))
        graph[end].append((start,1))
    
    for s in sources:
        temp = dijkstra(n, s, graph)
        if temp[destination] == INF:
            answer.append(-1)
            continue
        answer.append(temp[destination])
        
    return answer

def dijkstra(n, start, graph):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for nextNode in graph[node]:
            nNode, nDist = nextNode
            cost = dist + nDist
            if cost < distance[nNode]:
                distance[nNode] = cost
                heapq.heappush(q, (cost, nNode))
        
    return distance
print(solution(3,[[1, 2], [2, 3]],[2, 3],1))
print(solution(5,[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],[1,3,5],5))
