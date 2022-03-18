import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split()))) 
# matrix = [list(map(int, input().split())) for _ in range(n)] 중요

q = deque([])
def bfs(n,m):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if n> nx >= 0 and m> ny >= 0 and not graph[nx][ny]:
                q.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j]) # 시작점 큐에 담기
        
bfs(n,m)

answer = 0
for i in graph:
    if 0 in i:
        answer = -1
        break
    else:
        answer = max(answer, max(i))

if answer == -1:
    print(-1)
else:
    print(answer-1)


