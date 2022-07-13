#
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().rstrip().split())
graph = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
	graph.append(list(map(int, input().rstrip().split())))

def bfs(x,y):
	dx = [0,0,-1,1]
	dy = [1,-1,0,0]
	q = deque((x,y,0))
	visited[x][y][0] = 1
	visited[x][y][1] = 1
	while q:
		x, y, z = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<= nx < n and 0 <= ny < m:
				if not visited[nx][ny][z] and graph[nx][ny] == 1 and z == 0:
					visited[nx][ny][z + 1] = visited[x][y][z] + 1
					z = 1
					q.append(nx,ny,z)
				elif not visited[nx][ny][z] and graph[nx][ny] == 1:
					visited[nx][ny][z]
