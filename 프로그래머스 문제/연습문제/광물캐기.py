from collections import deque
def solution(picks, minerals):
    
    answer = 0
    tiredList = [[1,1,1],[5,1,1],[25,5,1]]
    connectionDict = {
        "diamond":0,
        "iron" : 1,
		"stone" : 2
	}
    info = []
    minerals = minerals[:5 * sum(picks)]
    q = deque(minerals)
    while q:
        howManyDig = 0
        usedDia, usedIron, usedStone = 0,0,0
        while howManyDig < 5:
            howManyDig += 1
            mineral = q.popleft()
            usedDia += tiredList[0][connectionDict[mineral]]
            usedIron += tiredList[1][connectionDict[mineral]]
            usedStone += tiredList[2][connectionDict[mineral]]
            if not q:
                break
        info.append([usedDia,usedIron,usedStone])
    print(info)
    info.sort(key = lambda x : [x[2],x[1],x[0]])
    
    for idx, p in enumerate(picks):
        for _ in range(p):
            if info:
                answer += info.pop()[idx]
            else:
                return answer
            
    return answer
    
print(solution([1,3,2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0,1,1],["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))
print(solution([1,1,0],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone","iron", "iron", "diamond","diamond"]))