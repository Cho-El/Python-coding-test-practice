import heapq
class Participant:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
def solution(k, n, reqs):
    answer = 0
    waitingTimeTable = [[0] * (n - k + 2) for _ in range(k + 1)]
    mento = [1 for _ in range(k + 1)] # 멘토 배치 인원
    leftMentoNum = n - k
    typeParticipant = [[] for _ in range(k + 1)]
    
    for req in reqs:
        a,b,c = req
        typeParticipant[c].append(Participant(a,a + b))
    
    # 멘토 숫자별 기다리는 시간 테이블 완성
    calWaitingTime(typeParticipant, waitingTimeTable)
    
    # 멘토 배치
    while leftMentoNum > 0 :
        maxDim = -1
        maxType = -1
        for type in range(1, k + 1):
            first = waitingTimeTable[type][mento[type]]
            second = waitingTimeTable[type][mento[type] + 1]
            dif = first - second
            
            if maxDim < dif:
                maxType = type
                maxDim = dif
                
        mento[maxType] += 1
        leftMentoNum -= 1
    
    for type in range(1, k + 1):
        answer += waitingTimeTable[type][mento[type]]
            
    return answer

def calWaitingTime(typeGraph, timeTable):
    
    for mentoNum in range(1, len(timeTable[0])): # 멘토 숫자
        for type in range(1, len(timeTable)): # 상담 유형
            q = []
            waitingTime = 0
            for part in typeGraph[type]:
                if len(q) < mentoNum:
                    heapq.heappush(q, part.end)
                else:
                    minEnd = heapq.heappop(q)
                    if minEnd > part.start:
                        waitingTime += minEnd - part.start
                        heapq.heappush(q, part.end + minEnd - part.start)
                    else:
                        heapq.heappush(q, part.end)
            timeTable[type][mentoNum] = waitingTime
                
        
    
print(solution(3,5,[[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]))
print(solution(2,3,[[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))
