import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
cnt = 0

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()


def dfs2(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs2(i)

for i in range(1, N+1):
    if not visited[i]:
        dfs2(i)
        cnt += 1

print(cnt)

def dfs1(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            stack += graph[v]
    return True