def solution(players, callings):
    answer = []
    playersDict = {}
    for idx, p in enumerate(players):
        playersDict[idx] = p
    
    for c in callings:
        playersDict[c]
    return answer

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))