import heapq
def solution(k, score):
    answer = []
    q = []
    for s in score:
        # 길이가 k가 안될 때
        if len(q) != k:
            # 값을 넣는다.
            heapq.heappush(q,s)
            # 값을 넣고 answer에 첫번째 추가
            answer.append(q[0])
        # 길이가 k가 될 때
        else:
            # 힙에 들어 있는 가장 작은 값이 현재 들어온 수보다 작을 때
            if q[0] < s:
                heapq.heappop(q)
                heapq.heappush(q,s)
                answer.append(q[0])
            else:
                answer.append(q[0])
    return answer