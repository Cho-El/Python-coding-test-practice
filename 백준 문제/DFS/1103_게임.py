import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())
graph = []
for i in range(n):
    temp = list(input().rstrip())
    graph.append(temp)

visited = [[False for _ in range(m)] for _ in range(n)]
dp = [[0] * m for _ in range(n)]

dx = [0,0,1,-1] # 상, 하, 우, 좌
dy = [1,-1,0,0]

final_answer = 0

# dp 만 사용한 풀이 -> 시간 초과
# def dfs(x,y,answer):
#     global final_answer
#     if final_answer == -1:
#         return

#     final_answer = max(final_answer, answer + 1)
#     visited[x][y] = True
#     for i in range(4):
#         nx = x + dx[i] * int(graph[x][y])
#         ny = y + dy[i] * int(graph[x][y])
#         if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'H':
#             if visited[nx][ny]:
#                 print(-1)
#                 exit()
#             dfs(nx, ny, answer + 1)
#             visited[nx][ny] = False

def dfs(x,y,answer):
    global final_answer
    if final_answer == -1:
        return

    final_answer = max(final_answer, answer + 1)
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i] * int(graph[x][y])
        ny = y + dy[i] * int(graph[x][y])
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'H' and answer + 1 > dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()
            dp[nx][ny] = answer + 1
            dfs(nx, ny, answer + 1)
            visited[nx][ny] = False

dfs(0,0,0)
print(final_answer)