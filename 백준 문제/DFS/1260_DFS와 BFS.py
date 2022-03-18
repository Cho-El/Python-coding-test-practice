from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

def dfs1(V):
    if visited1[V] != 0 :
        return
    
    visited1[V] = 1
    print(V, end = ' ')
    for i in graph[V]:
        dfs1(i)

def dfs2(V):
    stack = [V]
    for i in graph:
        i.sort(reverse = True)
    while stack:
        v = stack.pop()
        if visited1[v] == 0:
            print(v, end = ' ')
            visited1[v] = 1
            stack += graph[v]


def bfs(V):
    for i in graph:
        i.sort()
    q = deque([V])
    visited2[V] = 1
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visited2[i] == 0:
                q.append(i)
                visited2[i] = 1




dfs2(V)
print()
bfs(V)