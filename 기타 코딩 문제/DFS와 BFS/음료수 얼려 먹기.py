'''
N X M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는
부분은 1로 표시됩니다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결
되어 있는 것으로 간주합니다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
다음의 4 X 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.

ex)
세로 길이 N과 가로 길이 M
두 번째 줄부터는 N +1번째 줄까지 얼음 틀의 형태가 주어집니다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.
한번에 만들 수 있는 아이스크림의 개수를 출력합니다.

4 5
00110
00011
11111
00000

출력 3

'''
import copy
N, M = map(int,input("크기는 ?").split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(N):
	graph.append(list(map(int, input())))
graph2 = copy.deepcopy(graph)

def dfs(x, y,n,m):
	if x <= -1 or x >= n or y <= -1 or y >= m :
		return False

	if graph[x][y] == 0:
		graph[x][y] = 1
		dfs(x-1,y,n,m)
		dfs(x,y-1,n,m)
		dfs(x+1,y,n,m)
		dfs(x,y+1,n,m)
		return True
	return False

def ice_cream(N,M):
	result = 0
	for i in range(N):
		for j in range(M):
			if dfs(i,j,N,M) == True:
				result += 1
	return result

print(ice_cream(N,M))

# print(graph2)
from collections import deque
def bfs(x, y,n,m):
	if graph2[x][y] == 1:
		return False
	queue = deque([[x,y]])
	
	while queue :
		v = queue.popleft()
		x, y = v[0], v[1]

		if x <= -1 or x >= n or y <= -1 or y >= m :
			continue 
		if graph2[x][y] == 1:
			continue

		if graph2[x][y] == 0:
			graph2[x][y] = 1
			queue.append([x-1,y])
			queue.append([x,y-1])
			queue.append([x+1,y])
			queue.append([x,y+1])

	return True

def ice_cream_bfs(N,M):
	result = 0
	for i in range(N):
		for j in range(M):
			if bfs(i,j,N,M) == True:
				result += 1
	
	return result

print(ice_cream_bfs(N,M))
