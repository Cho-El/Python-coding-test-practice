# 트리 dfs
# 증명 임의의 점 a에서 가장 먼 x를 찾고 x에서 가장 먼 y를 찾으면 x,y의 거리가 트리의 지름이다.
# 시간초과 ----------------------------------------------
# import sys
# input = sys.stdin.readline
# n = int(input())
# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# result = 0

# for _ in range(n):
#     temp = list(map(int, input().rstrip().split()))
#     start = temp[0]
#     temp_t = temp[1:-1]
#     for i in range(0,len(temp_t),2):
#         graph[start].append((temp_t[i], temp_t[i + 1]))

# def dfs(start, dist):
#     global result, visited
#     result = max(result, dist)
#     visited[start] = True
#     can_visit = 0
    
#     for next_node in graph[start]:
#         node, edge = next_node
#         if not visited[node]:
            
#             dist += edge
#             dfs(node, dist)
#             visited[node] = False
#             dist -= edge

# for i in range(1, n + 1):
#     dfs(i, 0)

# print(result)

# 두번째 풀이
import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    start = temp[0]
    temp_t = temp[1:-1]
    for i in range(0,len(temp_t),2):
        graph[start].append((temp_t[i], temp_t[i + 1])) # 정점, 거리

edge_dist = [0 for _ in range(n + 1)]

def dfs(start, dist):
    global visited
    visited[start] = True
    for edge, weight in graph[start]:
        if not visited[edge]:
            edge_dist[edge] = dist + weight
            dfs(edge, dist + weight)
            
dfs(1, 0)
longest_edge = edge_dist.index(max(edge_dist))

edge_dist = [0 for _ in range(n + 1)]
visited = [False] * (n + 1)
dfs(longest_edge, 0)
print(max(edge_dist))