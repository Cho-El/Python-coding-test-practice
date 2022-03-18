import sys
sys.setrecursionlimit(10 ** 6)
T = int(input())
def dfs(graph,y,x,m,n):
    if y < 0 or x < 0 or y >=n or x >= m:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(graph, y - 1, x, m, n) # 상
        dfs(graph, y + 1, x, m, n)# 하
        dfs(graph, y, x - 1, m, n)# 좌
        dfs(graph, y, x + 1, m, n)# 우
        return True
    
    return False

def gimchi():
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0

    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                if dfs(graph,j,i,m,n):
                    cnt += 1
    
    print(cnt)

for _ in range(T):
    gimchi()