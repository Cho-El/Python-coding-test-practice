import heapq
def solution(jobs):
    start,now, answer, i = -1, 0, 0, 0 # 이전에 완료한 시간, 
    h = []
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <=now:
                heapq.heappush(h, (job[1],job[0])) # 사이에 있으면 삽입
        if h: # 힙에 데이터가 들어가 있으면
            work = heapq.heappop(h)
            start = now
            now += work[0]
            answer += now - work[1]
            i += 1
        else:
            now += 1
    
    return answer//len(jobs)
