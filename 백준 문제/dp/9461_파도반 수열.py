# dp 수학
# dp 문제는 갯수만큼 테이블을 설정하자!
import sys
def solution(n):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2]
    
    return dp[n]
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solution(n))