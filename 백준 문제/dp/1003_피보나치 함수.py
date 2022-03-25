import sys
t = int(input())
def fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)
	
for i in range(t):
	n = int(input())
	dp = [(0,0) for _ in range(n+1)]
	if n == 0:
		print(1, 0)
		continue
	if n == 1:
		print(0, 1)
		continue

	dp[0] = (1,0)
	dp[1] = (0,1)
	for i in range(2,n+1):
		dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
	a, b = dp[n]
	print(a,b)