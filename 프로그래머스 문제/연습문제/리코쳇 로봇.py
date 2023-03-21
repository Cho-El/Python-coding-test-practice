import sys
# sys.setrecursionlimit(10 ** 6)
def solution(board):
	global result
	global visited
	lenX = len(board)
	lenY = len(board[0])
	INF = sys.maxsize

	visited = [[INF for _ in range(lenY)] for _ in range(lenX)]
	
	result = INF
	for x in range(lenX):
		for y in range(lenY):
			if board[x][y] == 'R':
				dfs(x, y, lenX, lenY, board, 0)
	
	if result == INF:
		return -1
	return result

def dfs(x,y,lenX,lenY,board,distance):
	global result
	global visited

	dx = [0,0,1,-1]
	dy = [1,-1,0,0]
	
	if board[x][y] == 'G':
		result = min(result, distance)
		return
	
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if 0 <= nx < lenX and 0 <= ny < lenY and board[nx][ny] != 'D':
			while 0 <= nx + dx[i] < lenX and 0 <= ny + dy[i] < lenY and board[nx + dx[i]][ny + dy[i]] != 'D':
				nx += dx[i]
				ny += dy[i]
			
			if visited[nx][ny] > distance + 1:
				visited[nx][ny] = min(visited[nx][ny], distance + 1)
			else:
				continue

			dfs(nx, ny, lenX, lenY, board, distance + 1)
		
		


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))
