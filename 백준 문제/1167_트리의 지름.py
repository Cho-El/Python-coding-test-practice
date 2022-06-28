#
import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = 0

for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    start = temp[0]
    temp_t = temp[1:-1]
    for i in range(0,len(temp_t),2):
        graph[start].append((temp_t[i], temp_t[i + 1]))

def dfs(start, dist):
    global result, visited
    result = max(result, dist)
    visited[start] = True
    can_visit = 0
    
    for next_node in graph[start]:
        node, edge = next_node
        if not visited[node]:
            
            dist += edge
            dfs(node, dist)
            visited[node] = False
            dist -= edge

for i in range(1, n + 1):
    dfs(i, 0)

print(result)