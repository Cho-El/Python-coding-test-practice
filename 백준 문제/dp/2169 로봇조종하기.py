import sys
input = sys.stdin.readline
n,m = map(int, input().split())
MININF = -sys.maxsize
dp = [[MININF for _ in range(m)] for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,1]
dy = [-1,1,0]
dp[0][0] = graph[0][0]

# 첫째 행 업데이트
'''
첫째 행은 오른쪽으로만 업데이트
'''
dp[0][0] = graph[0][0]
for i in range(1,m):
    dp[0][i] = dp[0][i - 1] + graph[0][i]
# 그 밖의 행
for x in range(1,n):
    tmp = [[MININF for _ in range(m)] for _ in range(2)]
    # 왼쪽에서 오른쪽
    tmp[0][0] = dp[x - 1][0] + graph[x][0]
    for y in range(1,m):
        tmp[0][y] = max(dp[x - 1][y], tmp[0][y - 1]) + graph[x][y]
    # 오른쪽에서 왼쪽
    tmp[1][m - 1] = dp[x - 1][m - 1] + graph[x][m - 1]
    for y in range(m - 2, -1, -1):
        tmp[1][y] = max(dp[x - 1][y], tmp[1][y + 1]) + graph[x][y]
    # 값 비교 후 업데이트
    for idx, (tmp1, tmp2) in enumerate(zip(tmp[0],tmp[1])):
        dp[x][idx] = max(tmp1, tmp2)

print(dp[-1][-1])
