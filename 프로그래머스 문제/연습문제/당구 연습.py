import sys

def calDistance(x1,y1, x2,y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def solution(m, n, startX, startY, balls):
	INF = sys.maxsize
	answer = []
	for bx,by in balls:
		up,down,left,right = INF,INF,INF,INF
		# 상으로 뒤집을 때
		if not (startX == bx and startY < by):
			up = calDistance(startX, startY, bx, 2 * n - by)
		# 하로 뒤집을 떄
		if not (startX == bx and startY > by):
			down = calDistance(startX, startY, bx, -by)
		# 좌로 뒤집을 떄
		if not (startY == by and startX > bx):	
			left = calDistance(startX, startY, -bx, by)
		# 우로 뒤집을 떄
		if not (startY == by and startX < bx):
			right = calDistance(startX, startY, 2 * m - bx, by)
		answer.append(min(up,down,left,right))

	return answer

print(solution(10,10,3,7,[[2,7],[7,7],[7,3]]))