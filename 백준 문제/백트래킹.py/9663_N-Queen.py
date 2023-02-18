#
import sys
n = int(input())
result = 0
board = [0] * n

def dfsQ(row):
	global result
	# 종료 조건 row가 n까지 찼을 떄
	if row == n:
		result += 1
		return
    # 행단위로 체크
	for i in range(n):
		board[row] = i
		# 그 위치에 퀸을 놔도 되는지 체크
		if check(row):
			dfsQ(row + 1)

def check(row):
	# 상하 대각선 체크
	for comp_row in range(row):
		if board[comp_row] == board[row] or abs(board[row] - board[comp_row]) == abs(row - comp_row):
			return False
	return True

dfsQ(0)
print(result)