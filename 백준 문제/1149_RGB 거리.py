# dp
import sys
input = sys.stdin.readline
n = int(input())
rgb = []
for _ in range(n):
    rgb.append([int(i) for i in input().rstrip().split()])

dp = [[float('inf')] * 3 for _ in range(n)]

for i in range(3):
    dp[0][i] = rgb[0][i]

for i in range(n-1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i + 1][j] = min(dp[i][k] + rgb[i + 1][j], dp[i + 1][j])

print(min(dp[n-1]))