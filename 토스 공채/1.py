def solution(s, N):
    answerList = []
    rangeNum = list(range(1,N + 1))
    for i in range(len(s) - N + 1):
        testStr = s[i : i + N]
        testSet = set(testStr)
        if len(testSet) != len(testStr):
            continue
            
        for t in testStr:
            if int(t) not in rangeNum:
                break
        else:
            answerList.append(int(testStr))
            
    if answerList:
        return max(answerList)
    else:
        return -1


print(solution("313253123", 3))