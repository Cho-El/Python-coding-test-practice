#
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
# 0 - 북, 1 - 동, 2- 남, 3 - 서
r,c,d = map(int, input().split())
graph = []
dx = [-1,0,1,0] # 남, 동, 북, 서
dy = [0,1,0,-1]

for i in range(n):
    graph.append(list(map(int, input().split())))

def checkGoBack(x, y, d, MAP):
    nd = (d + 2) % 4 # 뒤로 가기
    nx, ny = x + dx[nd], y + dy[nd]
    if MAP[nx][ny] == 1:
        return False
    return nx, ny

def checkLeft(nx, ny):
    if graph[nx][ny] == 0:
        if 1 <= nx < n - 1 and 1 <= ny < m - 1:
            return True
    else:
        return False
    
def bfs(r,c,d,graph):
    mapTemp = 2
    q = deque()
    q.append([r,c,d])
    
    while q:
        x,y,d = q.popleft()
        graph[x][y] = mapTemp
        nowD = d
        for i in range(4):
            nowD -= 1
            if nowD == -1:
                nowD = 3
            nx, ny = x + dx[nowD], y + dy[nowD]
            if checkLeft(nx,ny):
                mapTemp += 1
                q.append((nx,ny,nowD))
                break
            elif i == 3:
                result = checkGoBack(x,y,d,graph)
                if not result:
                    return mapTemp - 1
                else:
                    nx, ny = result
                    q.append((nx,ny,d))
                    
print(bfs(r,c,d,graph))