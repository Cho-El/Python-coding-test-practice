def solution(picks, minerals):
    global answer
    answer = 0
    tiredList = [[1,1,1],[5,1,1],[25,5,1]]
    connectionDict = {
        "diamond":0,
        "iron" : 1,
		"stone" : 2
	}
    
    return answer

def dfs(tiredList, connectionDict, picks, minerals, startMinerals, usedTool):
    global answer
    if 
    for i in range(3):
        if picks[i] == 0:
            continue
        else:
            picks[0] -= 1
            usedTool.append(i)
            dfs(tiredList, connectionDict, picks,minerals,usedTool)
            
            
    
print(solution([1,3,2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))