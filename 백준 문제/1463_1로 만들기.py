n = int(input())

dp = [0] * (10**6 + 1)
di = [2,3]

for i in range(2,n+1):
	dp[i] = dp[i-1] + 1
	for j in di:
		if i % j == 0:
			dp[i] = min(dp[i], dp[i//j] + 1)

print(dp[n])