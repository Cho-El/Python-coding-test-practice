# 비트마스킹
import sys
input = sys.stdin.readline
n = int(input())
W = []

for _ in range(n):
	W.append([int(i) for i in input().rstrip().split()])

dp = [[0] * (1<<n) for _ in range(n)]
done = (1<<n) - 1

def dfs(cur, visited):
	if visited == done:
		return W[cur][0] if W[cur][0] != 0 else float('inf')
	
	if dp[cur][visited] != 0:
		return dp[cur][visited]
	
	cost = float('inf')
	for next_city in range(1, n):
		if W[cur][next_city] == 0 or visited & (1 << next_city) > 0:
			continue
		cost = min(cost, dfs(next_city, visited | (1 << next_city)) + W[cur][next_city])
	dp[cur][visited] = cost
	
	return cost

print(dfs(0,1))