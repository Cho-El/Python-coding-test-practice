#
import sys
input = sys.stdin.readline
n = int(input())
grape = []
dp = [0 for _ in range(n)]
for _ in range(n):
    grape.append(int(input()))

if n == 1:
    dp[0] = grape[0]
elif n == 2:
    dp[0] = grape[0]
    dp[1] = grape[0] + grape[1]
else:
    dp[0] = grape[0]
    dp[1] = grape[0] + grape[1]
    dp[2] = max(grape[0] + grape[1], grape[0] + grape[2], grape[1] + grape[2])


for i in range(3, n):
    dp[i] = max(dp[i-3] + grape[i-1] + grape[i], dp[i-2] + grape[i], dp[i-1])

print(dp[n-1])