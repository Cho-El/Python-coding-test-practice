import sys
input = sys.stdin.readline
n,k = map(int, input().split())
bag = [[0,0]]
for _ in range(n):
    bag.append(list(map(int, input().split())))

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(1,n + 1):
    for j in range(1, k + 1):
        weight = bag[i][0]
        value = bag[i][1]
        if weight > j: # 못 넣는 경우
            dp[i][j] = dp[i - 1][j]
        else: # 넣을 수 있는 경우
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])

print(dp[n][k])

