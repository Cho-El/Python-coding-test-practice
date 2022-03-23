import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
graph = []
visited = []
result = 0

for _ in range(n):
	graph.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(x,y,h):
	global result
	
	dx = [-1,0,0,1]
	dy = [0,-1,1,0]
	q = deque([(x,y)])
	visited[x][y] = 1
	pool = True
	cnt = 1
	while q:
		x, y = q.popleft()
		for _ in range(4):
			nx = x + dx[_]
			ny = y + dy[_]
			if nx < 0 or ny <0 or nx >=n or ny >=m:
				pool = False
				continue
			
			if graph[nx][ny] < h and not visited[nx][ny] :
				visited[nx][ny] = 1
				q.append((nx,ny))
				cnt += 1
		
	if pool:
		result += cnt
	return


for h in range(1,10):
	visited = [[0] * m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if graph[i][j] < h and not visited[i][j]:
				bfs(i,j,h)

print(result)