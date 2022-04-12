#
import sys
sys.setrecursionlimit(10**6) # 깊이 주의

def dfs(x,y, graph,visited):
    visited[x][y] = 1
    for i in range(4):
        nextx = x + dx[i]
        nexty = y + dy[i]
        if 0 <= nextx < len(graph) and 0 <= nexty < len(graph) and not visited[nextx][nexty] \
            and graph[nextx][nexty] == graph[x][y]:
            dfs(nextx,nexty,graph,visited)


def solution(graph):
    visited = [[0]*len(graph) for _ in range(len(graph))]
    result = []
    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if not visited[i][j]:
                dfs(i,j,graph,visited)
                cnt += 1
    result.append(cnt)

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'

    visited = [[0]*len(graph) for _ in range(len(graph))]
    cnt = 0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if not visited[i][j]:
                dfs(i,j,graph,visited)
                cnt += 1
    
    result.append(cnt)
    return result

if __name__ == "__main__":
    n = int(input())
    graph = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for _ in range(n):
        graph.append(list(sys.stdin.readline().rstrip()))
    a = solution(graph)
    for i in a:
        print(i, end = ' ')