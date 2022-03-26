import sys
n = int(input())
p = list(map(int, sys.stdin.readline().split()))
m = int(input())
dp = [-1] * (51)
min_cost = min(p)

for i in range(len(p)): # dp 초기화
	dp[p[i]] = max(dp[p[i]],i)

for j in range(min_cost, m+1):
	for i in range(n):
		if j-p[i] > 0 and dp[j-p[i]] != -1:
			temp = []
			temp.append(str(dp[j - p[i]]))
			temp.append(str(dp[p[i]]))
			temp.sort(reverse = True)
			value = int(''.join(temp))
			dp[j] = max(dp[j],value)


print(max(dp[:m+1]))