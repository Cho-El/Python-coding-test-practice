n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
cnt = 0
visited = [0] * (n + 1)
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse = True)

def dfs(v,cnt):
    stack = [v]
    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
            cnt += 1
            stack += graph[v]
    return cnt-1
            

print(dfs(1,cnt))