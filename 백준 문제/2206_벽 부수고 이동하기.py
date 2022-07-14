# bfs 응용
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().rstrip().split())
graph = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
	graph.append([int(i) for i in input().rstrip()])

def bfs(x,y):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    q = deque([(x,y,0)])
    visited[x][y][0] = 1
    
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z == 0:
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    q.append((nx,ny,z + 1))
                    
                elif not visited[nx][ny][z] and graph[nx][ny] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
    
    return -1

print(bfs(0,0))