
# 시간 초과 풀이
# import sys
# import heapq
# from copy import deepcopy

# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# INF = sys.maxsize
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     start,end,cost = map(int, input().split())
#     graph[start].append([end,cost])
# targetS, targetE = map(int, input().split())

# def dijkstra(targetS):
#     distance = [[INF,[]] for _ in range(n + 1)]
#     q = []
#     heapq.heappush(q, [0, targetS,[targetS]])
#     while q:
#         dist, node, trace = heapq.heappop(q)
#         if distance[node][0] < dist:
#             continue
        
#         for nextNode in graph[node]:
#             nNode, cost = nextNode
#             nCost = cost + dist
#             if distance[nNode][0] >= nCost:
#                 newTrace = deepcopy(trace)
#                 if nNode not in newTrace:
#                     newTrace.append(nNode)
#                 if distance[nNode][0] == nCost:
#                     distance[nNode][1].append(newTrace)
#                     heapq.heappush(q, [nCost, nNode, newTrace])
#                 else:
#                     distance[nNode][0] = nCost
#                     distance[nNode][1] = [newTrace]
#                     heapq.heappush(q, [nCost, nNode, newTrace])
    
#     return distance


# result = dijkstra(targetS)
# print(result[targetE][0])
# print(len(result[targetE][1][0]))
# print(*result[targetE][1][0])

# 두번째 풀이
# import sys
# import heapq
# from copy import deepcopy

# input = sys.stdin.readline
# n = int(input())
# m = int(input())
# INF = sys.maxsize
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     start,end,cost = map(int, input().split())
#     graph[start].append([end,cost])
# targetS, targetE = map(int, input().split())

# def dijkstra(targetS):
#     distance = [[INF,[]] for _ in range(n + 1)]
#     q = []
#     heapq.heappush(q, [0, targetS,[targetS]])
#     while q:
#         dist, node, trace = heapq.heappop(q)
#         if distance[node][0] < dist:
#             continue
        
#         for nextNode in graph[node]:
#             nNode, cost = nextNode
#             nCost = cost + dist
#             if distance[nNode][0] > nCost:
#                 distance[nNode][0] = nCost
#                 newTrace = deepcopy(trace)
#                 if nNode not in newTrace:
#                     newTrace.append(nNode)
#                 distance[nNode][1] = newTrace
#                 heapq.heappush(q, [nCost, nNode, newTrace])
    
#     return distance


# result = dijkstra(targetS)
# print(result[targetE][0])
# print(len(result[targetE][1]))
# print(*result[targetE][1])

# 다른 사람 풀이1
# import sys
# input = sys.stdin.readline
# from heapq import heappop, heappush

# def sol(n: int, m: int) -> str:
#     INF = sys.maxsize
#     graph = [{} for _ in range(n+1)]
#     for _ in range(m):
#         a,b,c = map(int, input().split())
#         if b in graph[a]:
#             if c < graph[a][b]:
#                 graph[a][b] = c
#             continue
#         graph[a][b] = c
        
#     start,end = map(int, input().split())
#     dist = [INF] * (n+1)
#     dist[start] = 0
#     path = [0] * (n+1)
#     q = [(0,start)]

#     while q:
#         p_c,p_n = heappop(q)
#         if p_c > dist[p_n]:
#             continue
        
#         for c_n,c_c in graph[p_n].items():
#             n_c = p_c+c_c
#             if n_c < dist[c_n]:
#                 dist[c_n] = n_c
#                 path[c_n] = p_n
#                 heappush(q, (n_c,c_n))

#     temp = str(dist[end])
#     ans = [str(end)]
#     while path[end]:
#         end = path[end]
#         ans.append(str(end))

#     return '\n'.join((temp, str(len(ans)), ' '.join(reversed(ans))))


# print(sol(int(input()), int(input())))

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