from collections import deque
def solution(maps):
    global visited
    answer = 0
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    finalCountry = {}
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != '.':
                tempC = bfs(i,j,len(maps),len(maps[0]),maps)
                for t in tempC:
                    if t not in finalCountry:
                        finalCountry[t] = tempC[t]
                    else:
                        finalCountry[t] += tempC[t]
    
    for value in finalCountry.values():
        answer = max(answer, value)
        
    return answer

def bfs(x,y,maxX,maxY, maps):
    global visited
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque([[x,y]])
    visited[x][y] = True
    Country = {
        maps[x][y] : 1
    }
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < maxX and 0 <= ny < maxY and maps[nx][ny] != '.' and not visited[nx][ny]:
                if maps[nx][ny] not in Country:
                    Country[maps[nx][ny]] = 1
                    visited[nx][ny] = True
                    q.append([nx,ny])
                else:
                    Country[maps[nx][ny]] += 1
                    visited[nx][ny] = True
                    q.append([nx,ny])
    
    maxTemp = 0
    for value in Country.values():
        maxTemp = max(maxTemp, value)
    maxCountry = []
    for key, value in Country.items():
        if value == maxTemp:
            maxCountry.append(key)
    maxCountry.sort()
    winnerCountry = maxCountry[-1]
    
    for key in Country.keys():
        if key not in maxCountry:
            Country[winnerCountry] += Country[key]
    
    resultCountry = {}
    for i in maxCountry:
        resultCountry[i] = Country[i]
        
    return resultCountry

g = ["AABCA.QA", "AABC..QX","BBBC.Y..",".A...T.A","....EE..", ".M.XXEXQ","KL>TBBBQ"]
print(solution(g))