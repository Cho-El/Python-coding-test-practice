# 트리
# 트리는 사이클이 없는 무방향 그래프이다.
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
edge_list = [0] * (n + 1)

for _ in range(n-1):
    a,b,c = map(int, input().rstrip().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
    
def dfs(start, dist):
    visited[start] = True    
    for next,w in graph[start]:
        if not visited[next]:
            edge_list[next] = w + dist
            dfs(next, w + dist)

dfs(1, 0)
temp_idx = edge_list.index(max(edge_list))

visited = [False] * (n + 1)
edge_list = [0] * (n + 1)
dfs(temp_idx, 0)
print(max(edge_list))