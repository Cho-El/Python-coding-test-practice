def solution(players, callings):
    answer = []
    playersDict = {}
    for idx, p in enumerate(players):
        playersDict[p] = idx
    
    for c in callings:
        curIdx = playersDict[c]
        nextIdx = curIdx - 1
        playersDict[c] = nextIdx
        playersDict[players[nextIdx]] = curIdx
        players[curIdx], players[nextIdx] = players[nextIdx], players[curIdx]
        
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))