import sys
sys.setrecursionlimit(10 ** 6)
def solution(n, m, x, y, r, c, k):
    global answer
    answer = "impossible"
    shortestDistance = abs(x - r) + abs (y - c)
    visited = [[['' for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    dfs(n,m,x - 1,y - 1,r - 1,c - 1,k,visited,shortestDistance)
    return answer

def dfs(n,m,x,y,r,c,k,visited,shortestDistance):
    global answer
    direction = {
        'd':(1,0),
        'l':(0,-1),
        'r':(0,1),
        'u':(-1,0)
    }
    if k == 0:
        if (x == r) and (y == c):
            answer = visited[x][y][0]
        return
    
    distToTarget = abs(x - r) + abs(y - c)
    if distToTarget <= k and distToTarget % 2 == k % 2: # 이 코드로 시간 초과 해결
        for key, value in direction.items():
            nx = x + value[0]
            ny = y + value[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][k - 1]:
                if abs(nx - r) + abs(ny - c) <= k - 1:
                    visited[nx][ny][k - 1] += visited[x][y][k] + key
                    dfs(n,m, nx, ny, r, c, k - 1,visited,shortestDistance)
                    if answer != "impossible":
                        return
    return

print(solution(3,4,2,3,3,1,5))
print(solution(2,2,1,1,2,2,2))
print(solution(3,3,1,2,3,3,4))
