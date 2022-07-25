import sys
import math

def solution(n):
    dp = [i for i in range(105)]
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, int(math.sqrt(i) + 1)):
            if j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
    
    return dp[n]

if __name__ == '__main__':
    for s in range(105):
        print(solution(s))
    