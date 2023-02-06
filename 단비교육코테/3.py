def solution(v):
    global area, size
    maxSize = 0
    area = 0
    for x in range(len(v)):
        for y in range(len(v[0])):
            if v[x][y] == 1:
                size = 0
                dfs(x,y,v)
                if size > maxSize:
                    maxSize = size
                area += 1
    result = [area,maxSize]
    return result

def dfs(x,y,v):
    global size
    size += 1
    v[x][y] = 0
    xLen = len(v)
    yLen = len(v[0])
    # 순회
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < xLen and 0 <= ny < yLen and v[nx][ny] == 1:
            dfs(x,y,v)

    return
print(solution([[1,1,0,1,1],[0,1,1,0,0],[0,0,0,0,0],[1,1,0,1,1],[1,0,1,1,1],[1,0,1,1,1]]))