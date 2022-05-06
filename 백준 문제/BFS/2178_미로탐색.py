# 그래프 이론, 그래프 탐색, bfs
import sys
from collections import deque
def bfs(start):
    q = deque([start])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == 0 and ny == 0:
                continue
            if 0 <= nx <= n-1 and 0 <= ny <= m-1 and graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                q.append((nx,ny))





n,m = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

bfs((0,0))
print(graph[n-1][m-1])