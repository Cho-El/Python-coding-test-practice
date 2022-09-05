#
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n + 1)] # i번째가 무조건 동물이 들어가는 경우의 수
dp[0] = 1
dp[1] = 3
for i in range(2, n + 1):
    dp[i] = (dp[i-2] + dp[i-1]*2)

print(dp[n] % 9901)