import sys
input = sys.stdin.readline
n,m = map(int, input().split())
MININF = -sys.maxsize

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# # 풀이2
sys.setrecursionlimit(10 ** 6)
dp = [[[MININF] * 3 for _ in range(m)] for _ in range(n)]
dp[0][0] = [graph[0][0] for _ in range(3)]
direction = ((0,1),(0,-1),(1,0)) # 오른쪽, 왼쪽, 아래쪽
def dfs(x,y,z): # x, y, 전 방향 z
    # 첫 스타트인 경우 z = -1
    if z == -1:
        z = 0
    for i in range(3):
        nx = x + direction[i][0]
        ny = y + direction[i][1]
        if z == 0 and i == 1:
            continue
        if z == 1 and i == 0:
            continue
        if 0 <= nx < n and 0 <= ny < m:
            dp[nx][ny][i] = max(dp[nx][ny][i], dp[x][y][z] + graph[nx][ny])
            dfs(nx,ny,i)

dfs(0,0,-1)
print(max(dp[n - 1][m - 1]))
        


# 풀이 1
# dp = [[MININF for _ in range(m)] for _ in range(n)]
# dx = [0,0,1]
# dy = [-1,1,0]
# dp[0][0] = graph[0][0]

# # 첫째 행 업데이트
# '''
# 첫째 행은 오른쪽으로만 업데이트
# '''
# dp[0][0] = graph[0][0]
# for i in range(1,m):
#     dp[0][i] = dp[0][i - 1] + graph[0][i]
# # 그 밖의 행
# for x in range(1,n):
#     tmp = [[MININF for _ in range(m)] for _ in range(2)]
#     # 왼쪽에서 오른쪽
#     tmp[0][0] = dp[x - 1][0] + graph[x][0]
#     for y in range(1,m):
#         tmp[0][y] = max(dp[x - 1][y], tmp[0][y - 1]) + graph[x][y]
#     # 오른쪽에서 왼쪽
#     tmp[1][m - 1] = dp[x - 1][m - 1] + graph[x][m - 1]
#     for y in range(m - 2, -1, -1):
#         tmp[1][y] = max(dp[x - 1][y], tmp[1][y + 1]) + graph[x][y]
#     # 값 비교 후 업데이트
#     for idx, (tmp1, tmp2) in enumerate(zip(tmp[0],tmp[1])):
#         dp[x][idx] = max(tmp1, tmp2)

# print(dp[-1][-1])

# import sys

# # 재귀깊이 해제
# sys.setrecursionlimit(100000)

# # go : 현재 (x, y)에서 이전 방향이 z였을 때 얻을 수 있는 최대값을 리턴하는 함수
# def go(x, y, z):
#     # Base Case : 오른쪽 아래에 도달한 경우
#     if x == n - 1 and y == m - 1:
#         return arr[x][y]
        
#     # Memoization
#     if dp[x][y][z] != -1:
#         return dp[x][y][z]
        
#     # 음의 무한대로 초기화
#     dp[x][y][z] = -9876543210
    
#     for i in range(3):
#         # nx, ny : 다음 좌표
#         nx, ny = x + dx[i], y + dy[i]
        
#         # 오른쪽으로 왔다가 왼쪽으로 가는 경우, 왼쪽으로 왔다가 오른쪽으로 가는 경우는 continue
#         if z == 1 and i == 2:
#             continue
#         if z == 2 and i == 1:
#             continue
            
#         # 범위 확인 및 점화식
#         if 0 <= nx < n and 0 <= ny < m:
#             dp[x][y][z] = max(dp[x][y][z], go(nx, ny, i) + arr[x][y])
#     return dp[x][y][z]

# # 입력부
# n, m = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# # dx, dy : x좌표와 y좌표의 이동배열
# dx = [1,0,0]
# dy = [0,1,-1]

# # dp : 현재 (x, y)에서 이전 방향이 z였을 때 얻을 수 있는 최대값을 저장하는 상태 공간
# dp = [[[-1] * 4 for _ in range(m)] for _ in range(n)]

# # 정답 출력
# print(go(0,0,-1))