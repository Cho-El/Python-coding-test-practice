'''
동빈이는 N X M 크기의 직사각형 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어 이를
피해 탈출해야 합니다.
동빈이의 위치는(1,1)이며 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시 탈출할 수 있는
형태로 제시됩니다.
이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 시작 칸과 마지막
칸을 모두 포함해서 계산합니다.

bfs는 간선의 길이가 같을 때 최단 거리를 탐색하기 위해 사용할 수 있는 알고리즘이다.

미로탐색을 진행하는데, 이동할 때마다 가중치가 붙어서 이동한다거나, 이동 과정에서 
여러 제약이 있을 경우, DFS로 구현하는 것이 좋습니다.
탐색 시간은 더 걸리긴 하지만, 가중치에 대한 변수를 지속해서 관리할 수 있다는 장점이 있으므로 
코드 구현 시, 더 편리하기 때문입니다.

ex)
5 6
101010
111111
000001
111111
111111
출력 : 10
'''

from collections import deque
from copy import deepcopy

N,M = map(int, input("숫자를 입력해주세요").split())
graph = []
for i in range(N):
	graph.append(list(map(int,input())))
graph2 = deepcopy(graph)

def bfs(start,n,m): # 내 풀이 틀림
	cnt = 0
	queue = deque([start])
	while queue:
		v = queue.popleft() # x, y = queue.popleft()로도 씀
		x,y = v[0], v[1]
		if x== n and y == m:
			return cnt
		if x <= -1 or y <=-1 or x>=n or y>=m:
			continue
		if graph[x][y] == 0:
			continue

		else:
			
			graph[x][y] = 0
			queue.append((x+1,y))
			queue.append((x-1,y))
			queue.append((x,y+1))
			queue.append((x,y-1))
			cnt += 1

	return cnt

def escape(n,m):
	start = (0,0)
	print(bfs(start,n,m))

# escape(N,M)

dx = [-1,0,1,0]
dy = [0,-1,0,1]
def escape_bfs(start,n,m):
	queue = deque([start])

	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= n or ny <0 or ny >=m:
				continue
			if graph2[nx][ny] == 0:
				continue
			if graph2[nx][ny] == 1:
				graph2[nx][ny] = graph2[x][y]+1
				queue.append((nx,ny))

	return graph2[n-1][m-1]

print(escape_bfs((0,0),N,M))

def escape_dfs(start,n,m): # dfs의 경우 길어지면 
	x, y = start[0], start[1]

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		# 범위 벗어 날때
		if nx < 0 or nx >= n or ny <0 or ny >=m:
			continue
		# graph값이 0일때
		if graph[nx][ny] == 0:
			continue
		# graph 값이 1일때
		if graph[nx][ny] == 1:
			graph[nx][ny] = graph[x][y] + 1
			escape_dfs((nx,ny),n,m)
	
	return graph[n-1][m-1]


for i in graph2:
	print(i)
print(escape_dfs((0,0),N,M))
for i in graph:
	print(i)