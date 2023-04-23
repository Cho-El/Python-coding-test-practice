#
import sys
def checkEnd(startX, startY,targetStr, board):
	dx = [0,0,1,-1,1,1,-1,-1]
	dy = [1,-1,0,0,1,-1,1,-1]

	for i in range(8):
		moving = 1
		nx = startX
		ny = startY
		while True:
			nx += dx[i]
			ny += dy[i]
			if 0 <= nx < 3 and 0 <= ny < 3 and board[nx][ny] == targetStr:
				moving += 1
				continue
			else:
				break
		if moving == 3:
			return True
	
	return False


def solution(board):
	cntCircle = 0
	cntX = 0
	# 선 후공 실수하는 경우
	for b in board:
		for s in b:
			if s == "O":
				cntCircle += 1
			elif s == "X":
				cntX += 1
	
	# O의 개수 = X의 개수 + 1 or X의 개수 -> return 1
	if cntCircle == cntX + 1 or cntCircle == cntX:
		checkO = 0
		checkX = 0
		# 게임 종료 시점을 실수하는 경우
		for x in range(len(board)):
			for y in range(len(board[0])):
				if board[x][y] == "O":
					# O 빙고가 있을 때
					if checkEnd(x,y,'O',board):
						checkO += 1
				elif board[x][y] == "X":
					# X가 빙고가 있을 떄
					if checkEnd(x,y,'X',board):
						checkX += 1
		
		# O가 빙고가 있을 때
		if checkO != 0:
			# O의 개수와 X의 개수가 같은 경우
			if cntCircle == cntX:
				return 0
			else:
				if checkX != 0:
					return 0
				else:
					return 1
		# X 빙고가 있을 때
		elif checkX != 0:
			if cntCircle == cntX + 1:
				return 0
			else:
				return 1
		else:
			return 1
	else:
		return 0

print(solution(["OXO","XOO","XOX"]))
print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))
print(solution(["XOX", "OOO", "XOX"]))
print(solution([".OO", ".X.", "XX."]))