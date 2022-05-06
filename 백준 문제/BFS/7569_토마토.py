# 그래프 이론, 그래프 탐색, bfs
import sys
from collections import deque

def bfs(start):
    q = deque(start)
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            # 0인 경우 전파, 전 토마토에 + 1해서 대입
            if 0<= nx < n and 0<= ny <m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append([nz,nx,ny])


m,n,h = map(int,input().split())
graph = []
for i in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, sys.stdin.readline().split())))
    graph.append(temp)

start = []
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
dz = [1,-1,0,0,0,0]

for i in range(h):# z
    for j in range(n): # x
        for l in range(m): # y
            if graph[i][j][l] == 1:
                start.append([i,j,l])

bfs(start)

result = 0
for i in graph:
    for j in i:
        if 0 in j:
            print(-1)
            exit(0) # 
        result = max(result, max(j))

# for i in graph:
#     for j in i:
#         print(j)

if result == -1:
    print(-1)
else:
    print(result-1)