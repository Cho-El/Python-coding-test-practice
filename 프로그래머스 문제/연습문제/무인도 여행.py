# def solution(maps):
#     global food
#     answer = []
#     maps = [list(m) for m in maps]
#     lenX = len(maps)
#     lenY = len(maps[0])
#     for x in range(lenX):
#         for y in range(lenY):
#             if maps[x][y] != '0' and maps[x][y] != 'X':
#                 food = 0
#                 dfs(x,y,maps,lenX,lenY)
#                 answer.append(food)
                
#     return answer

# def dfs(x,y,maps,lenX,lenY):
#     global food
#     dx = [0,0,-1,1]
#     dy = [1,-1,0,0]
#     food += int(maps[x][y])
#     maps[x][y] = '0'
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx <lenX and 0 <= ny <lenY and maps[nx][ny] != '0' and maps[nx][ny] != 'X':
#             dfs(nx,ny,maps,lenX,lenY)
 
def solution(maps):
    answer = []
    maps = [list(m) for m in maps]
    lenX = len(maps)
    lenY = len(maps[0])
    for x in range(lenX):
        for y in range(lenY):
            if maps[x][y] != '0' and maps[x][y] != 'X':
                answer.append(dfs(x,y,0,maps,lenX,lenY))
                
    if not answer:
        return [-1]
    answer.sort()
    return answer

def dfs(x,y,food,maps,lenX,lenY):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    food += int(maps[x][y])
    maps[x][y] = '0'
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <lenX and 0 <= ny <lenY and maps[nx][ny] != '0' and maps[nx][ny] != 'X':
            food = dfs(nx,ny,food,maps,lenX,lenY)
    
    return food
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))