import heapq
def solution(scoville, K):
	cnt = 0
	heapq.heapify(scoville)

	while scoville[0] < K:
		try:
			heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
			cnt += 1
		except IndexError:
			return -1
	return cnt