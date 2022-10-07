# 힙
import sys, heapq
def solution(q,x):
	if x == 0:
		if q:
			print(-heapq.heappop(q))
			return
		else:
			print(0)
			return
	heapq.heappush(q,-x)
 
if __name__ == '__main__':
	n = int(input())
	q = []
	for _ in range(n):
		x = int(sys.stdin.readline())
		solution(q,x)