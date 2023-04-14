import sys
def solution(alp, cop, problems):
    
    INF = sys.maxsize
    targetAlp = -1
    targetCop = -1
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    
    for problem in problems:
        targetAlp = max(targetAlp, problem[0])
        targetCop = max(targetCop, problem[1])
    
    dp = [[INF for _ in range(targetCop + 1)] for _ in range(targetAlp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, targetAlp):
        for j in range(cop, targetCop):
            for problem in problems:
                alpReq, copReq, alpRwd, copRwd, cost = problem
                if i >= alpReq and j >= copReq and dp[i][j] != INF:
                    dp[i + alpRwd][j + copRwd] = min(dp[i][j] + cost, dp[i + alpRwd][j + copRwd])
                    
    return dp[targetAlp][targetCop]

print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))