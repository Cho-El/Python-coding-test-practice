N = int(input())
graph = []
result = []
cnt = 0
for i in range(N):
    graph.append(list(map(int, input())))
visited = [[0]* N for _ in range(N)]

def dfs(x,y,N):
    global cnt
    if x < 0 or y < 0 or x >= N or y >= N:
        return
    if graph[x][y] == 1 and not visited[x][y]:
        visited[x][y] = 1
        cnt += 1
        # 상
        dfs(x-1, y, N)
        # 하
        dfs(x+1,y,N)
        # 좌
        dfs(x,y-1,N)
        # 우
        dfs(x,y+1,N)

    return cnt


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]: # 1인곳에서 시작
            cnt = 0
            result.append(dfs(i,j,N))

print(len(result))
result.sort()
for i in result:
    print(i)