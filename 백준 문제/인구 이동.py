#
import sys
from collections import deque
input = sys.stdin.readline
n,L,R = map(int, input().rstrip().split())
graph = []
move_check = 0
result = 0
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))


def bfs(s_x,s_y,L,R,n):
    global move_check
    q = deque([[s_x,s_y]])
    total_population = graph[s_x][s_y]
    visited[s_x][s_y] = True
    temp = [[s_x,s_y]]
    check = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                check += 1
                total_population += graph[nx][ny]
                visited[nx][ny] = True
                q.append([nx,ny])
                temp.append([nx,ny])
    
    if check > 0:
        move_check = 1
        for x,y in temp:
            graph[x][y] = total_population//len(temp)

while True:
    move_check = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j,L,R,n)
    
    if not move_check:
        break
    else:
        result += 1
print(result)