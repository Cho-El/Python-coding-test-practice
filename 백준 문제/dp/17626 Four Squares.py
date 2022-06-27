# dp
import sys
import math
INF = sys.maxsize
input = sys.stdin.readline
n = int(input())

dp = [0,1]

for i in range(2, n + 1):
	min_v = INF
	for j in range(1,int(math.sqrt(i)) + 1):
		min_v = min(dp[i - j ** 2] + 1, min_v)
	dp.append(min_v)

print(dp[n])