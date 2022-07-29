
import sys
from collections import deque

answer = 0
input = sys.stdin.readline
n,m = map(int, input().rstrip().split())

graph = []
for _ in range(n):
	graph.append(list(map(int, input().rstrip().split())))

def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque([[0,0]])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny]:# 방문하였는데 치즈인경우
                    graph[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                graph[i][j] = 0
            elif graph[i][j] == 2:
                graph[i][j] = 1
                
def exist_cheese():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                return 1
    
    return 0

while exist_cheese():
    bfs()
    answer += 1
    
print(answer)
        
    
# import sys
# from collections import deque

# # 위 - 오 - 아래 - 왼 순서
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]

# H, W = map(int, sys.stdin.readline().split(" "))
# field = []

# for _ in range(H):
#     field.append(list(map(int, sys.stdin.readline().split(" "))))

# left = 0
# for i in range(H):
#     for j in range(W):
#         if field[i][j] == 1:
#             left += 1

# def bfs(left):
#     while queue:
#         now = queue.popleft()

#         for i in range(4):
#             ndr = now[0] + dr[i]
#             ndc = now[1] + dc[i]

#             if 0 <= ndr < H and 0 <= ndc < W and visited[ndr][ndc] == 0:
#                 visited[ndr][ndc] = 1

#                 # 치즈 가장자리를 만나면
#                 if field[ndr][ndc] == 1:
#                     field[ndr][ndc] = 2
#                     left -= 1
#                 else:
#                     queue.append([ndr, ndc])

#     return left


# def delete():
#     for i in range(H):
#         for j in range(W):
#             if field[i][j] == 2:
#                 field[i][j] = 0

# queue = deque()

# count = 0
# temp = left
# while left != 0:
#     visited = [[0 for _ in range(W)] for _ in range(H)]
#     queue.append([0, 0])
#     visited[0][0] = 1
#     left = bfs(left)

#     if left != 0:
#         temp = left

#     count += 1
#     for i in field:
#         print(i)
        
#     delete()

# print(count)
# print(temp)