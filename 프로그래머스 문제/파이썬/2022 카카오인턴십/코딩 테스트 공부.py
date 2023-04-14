import sys
def solution1(alp, cop, problems):
    
    INF = sys.maxsize
    targetAlp = -1
    targetCop = -1
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    
    for problem in problems:
        targetAlp = max(targetAlp, problem[0])
        targetCop = max(targetCop, problem[1])
    
    dp = [[INF for _ in range(cop + 2 * targetCop + 1)] for _ in range(alp + 2 * targetAlp + 1)]
    for i in range(alp + 1):
        for j in range(cop + 1):
            dp[i][j] = 0
    
    for i in range(alp, targetAlp + 1):
        for j in range(cop, targetCop + 1):
            for problem in problems:
                alpReq, copReq, alpRwd, copRwd, cost = problem
                if i >= alpReq and j >= copReq and dp[i][j] != INF:
                    dp[i + alpRwd][j + copRwd] = min(dp[i + alpRwd][j + copRwd], dp[i][j] + cost)
                    
    return dp[targetAlp][targetCop]

def solution2(alp, cop, problems):
    
    INF = sys.maxsize
    targetAlp = -1
    targetCop = -1
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    
    for problem in problems:
        targetAlp = max(targetAlp, problem[0])
        targetCop = max(targetCop, problem[1])
    
    dp = [[INF for _ in range(cop + 2 * targetCop + 1)] for _ in range(alp + 2 * targetAlp + 1)]
    for i in range(alp + 1):
        for j in range(cop + 1):
            dp[i][j] = 0
    
    for i in range(alp, targetAlp + 1):
        for j in range(cop, targetCop + 1):
            for problem in problems:
                alpReq, copReq, alpRwd, copRwd, cost = problem
                if i >= alpReq and j >= copReq:
                    dp[i + alpRwd][j + copRwd] = min(dp[i + alpRwd][j + copRwd], dp[i][j] + cost)
    
    answer = INF
    for i in range(targetAlp, len(dp)):
        for j in range(targetCop, len(dp[0])):
            answer = min(answer, dp[i][j])
            
    return answer

def solution3(alp, cop, problems):
    
    INF = sys.maxsize
    targetAlp = -1
    targetCop = -1
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    
    for problem in problems:
        targetAlp = max(targetAlp, problem[0])
        targetCop = max(targetCop, problem[1])
    
    dp = [[INF for _ in range(451)] for _ in range(451)]
    for i in range(alp + 1):
        for j in range(cop + 1):
            dp[i][j] = 0
    
    answer = []
    for i in range(alp, len(dp)):
        for j in range(cop, len(dp[0])):
            for problem in problems:
                alpReq, copReq, alpRwd, copRwd, cost = problem
                if i - alpRwd >= alpReq and j - copRwd >= copReq:
                    dp[i][j] = min(dp[i - alpRwd][j - copRwd] + cost, dp[i][j])
                    if i >= targetAlp and j >= targetCop:
                        answer.append(dp[i][j])

    return min(answer)

def solution(alp, cop, problems):
    
    INF = sys.maxsize
    targetAlp = -1
    targetCop = -1
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    
    for problem in problems:
        targetAlp = max(targetAlp, problem[0])
        targetCop = max(targetCop, problem[1])
    
    biggerCop = max(targetCop, cop)
    biggerAlp = max(targetAlp, alp)
    dp = [[INF for _ in range(biggerCop + 1)] for _ in range(biggerAlp + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, len(dp)):
        for j in range(cop, len(dp[i])):
            for problem in problems:
                alpReq, copReq, alpRwd, copRwd, cost = problem
                if i >= alpReq and j >= copReq:
                    nextAlp, nextCop = min(biggerAlp, i + alpRwd), min(biggerCop, j + copRwd)
                    dp[nextAlp][nextCop] = min(dp[nextAlp][nextCop], dp[i][j] + cost)

    return dp[-1][-1]

print(solution(1,1,[[0,2,1,1,100]]))
print(solution(0,0,[[4,3,1,1,100],[0,0,2,2,1]]))
print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
print(solution(20,20,[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,0,[[0,0,1,1,1],[150,150,1,1,100]]))
print(solution(1,1,[[0,2,1,1,100]]))