import sys
sys.setrecursionlimit(10 ** 6)
# 1번째 풀이
def solution1(x, y, n):
    global answer
    INF = sys.maxsize
    answer = INF
    dfs(0, y, n, x)

    if answer == INF:
        return -1
    else:
        return answer

def dfs(depth,y,n,opResult):
    global answer
    if opResult == y:
        answer = min(answer, depth)
        return
    elif opResult > y :
        return
    
    else:
        dfs(depth + 1, y, n, opResult + n)
        dfs(depth + 1, y, n, opResult * 2)
        dfs(depth + 1, y, n, opResult * 3)
        
# 2번쨰 풀이 DP
def solution(x, y, n):
    INF = 1000000
    dp = [INF for _ in range(y + 1)]
    dp[x] = 0
    for i in range(x + 1,y + 1):
        if i - n >= 0 and dp[i - n] != INF:
            dp[i] = min(dp[i], dp[i - n] + 1)
        if i % 2 == 0 and dp[i//2] != INF:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0 and dp[i//3] != INF:
            dp[i] = min(dp[i], dp[i//3] + 1)
    
    if dp[y] == INF:
        return -1
    else:
        return dp[y]


print(solution(10,40,5))
print(solution(10,40,30))
print(solution(2,5,4))
