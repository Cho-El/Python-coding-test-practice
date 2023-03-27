#
import sys
def solution(wall):
    result = []
    wallNearInfo = []
    for i in range(len(wall)):
        wall[i] = list(map(int, wall[i].split()))
    
    for x in range(len(wall)):
        start = 0
        temp = []
        for y in range(len(wall[x])):
            end = start + wall[x][y]
            wall[x][y] = [start,end]
            start = end
            temp.append(0)
        wallNearInfo.append(temp)
    
    for x in range(len(wall)):
        for y in range(len(wall[x])):
            if 0<= x + 1 < len(wall):
                for y2 in range(len(wall[x + 1])):
                    if wall[x][y][0] <= wall[x + 1][y2][0] < wall[x][y][1] or\
                        wall[x][y][0] < wall[x + 1][y2][1] <= wall[x][y][1] or\
                            wall[x + 1][y2][0] <= wall[x][y][0] <= wall[x + 1][y2][1] and\
                                wall[x + 1][y2][0] <= wall[x][y][1] <= wall[x + 1][y2][1]:
                                wallNearInfo[x][y] += 1
                                wallNearInfo[x + 1][y2] += 1

            if 0 <= y + 1 < len(wall[x]):
                wallNearInfo[x][y] += 1
                wallNearInfo[x][y + 1] += 1
    
    importantBlockNum = 0
    for w in wallNearInfo:
        importantBlockNum = max(importantBlockNum, max(w))

    for i in range(len(wallNearInfo)):
        for j in range(len(wallNearInfo[i])):
             if wallNearInfo[i][j] == importantBlockNum:
                  result.append([i,j])

    result.sort()
    return result

print(solution(["3 1 1 2", "2 3 2", "1 1 2 3"]))
print(solution(["1 1", "1 1"]))
print(solution(["1 1 1", "3"]))