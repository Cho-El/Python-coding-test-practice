#
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = []
result = 0

for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))


def dfs(x,y, h):
    global n
    visited[x][y] = True
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny <n and not visited[nx][ny] and graph[nx][ny] > h:
            visited[nx][ny] = True
            dfs(nx,ny,h)


for h in range(max(max,water_board)):
    visited = [[False] * n for _ in range(n)]
    temp = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and h < graph[x][y]:
                dfs(x,y,h)
                temp += 1
    result = max(result, temp)
    
print(result)