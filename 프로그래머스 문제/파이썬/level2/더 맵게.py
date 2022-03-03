import heapq
def solution2(scoville, K):
	cnt = 0
	heapq.heapify(scoville)

	while scoville[0] < K:
		try:
			heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
			cnt += 1
		except IndexError:
			return -1
	return cnt


def solution(scoville, K):
	cnt = 0
	heapq.heapify(scoville)

	while True:
		if scoville[0] >= K:
			break
		else:
			if len(scoville) <=1:
				return -1
			heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
			cnt += 1
	return cnt

K = 20
scoville = [1,2,3]
print(solution2(scoville, K))

