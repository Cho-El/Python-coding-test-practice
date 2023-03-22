from collections import deque
def solution(maps):
    global visited
    global arrivedOnLever
    arrivedOnLever = 0
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] == 'S':
                startX, startY = x,y
            elif maps[x][y] == 'E':
                endX, endY = x, y
    bfs(startX,startY,maps)

    if not arrivedOnLever:
        return -1
    else:
        if not visited[endX][endY]:
            return -1
        else:
            return visited[endX][endY]


def bfs(x,y,maps):
    global visited
    global arrivedOnLever
    q = deque([[x,y]])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] in {'O', 'L', 'E', 'S'}:
                if maps[nx][ny] == 'L':# Lever를 찾은 경우
                    q.clear()
                    temp = visited[x][y] + 1
                    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
                    visited[nx][ny] = temp
                    q.append([nx,ny])
                    arrivedOnLever = 1
                    break
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx,ny])
            
        
    
print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))
