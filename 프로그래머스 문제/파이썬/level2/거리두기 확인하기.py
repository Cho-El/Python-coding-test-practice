# 1번 풀이
# import sys
# dx = [0,0,-1,1] # 우좌상하
# dy = [1,-1,0,0]

# def dfs(places, x, y,depth):
#     if depth == 3: # depth 3까지 찾아봤는데 거리두기 잘 지키는 경우 True
#         return True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<= nx <5 and 0<= ny <5 and visited[nx][ny] == 0 and places[nx][ny] != 'X':
#             if places[nx][ny] == 'P':
#                 return False
#             else:
#                 visited[nx][ny] = 1
#                 if dfs(places,nx,ny,depth + 1):
#                     visited[nx][ny] = 0
#                 else:
#                     visited[nx][ny] = 0
#                     return False
    
#     return True
        

# def solution(places):
#     global visited
#     answer = []
#     for place in places:
#         flag = 0
#         visited = [[0] * 5 for _ in range(5)]
#         for i in range(5):
#             if flag == 1: # 이미 거리두기 안지키는 사람을 발견함
#                 break
#             for j in range(5):
#                 if place[i][j] == 'P' and not visited[i][j]:
#                     visited[i][j] = 1
#                     if dfs(place, i, j,1):
#                         continue
#                     else: # 거리두기 안지키는게 발견
#                         answer.append(0)
#                         flag = 1
#                         break
#         else:
#             answer.append(1)

#     return answer
#2번 풀이
import sys
dx = [0,0,-1,1] # 우좌상하
dy = [1,-1,0,0]

def dfs(place, x, y,depth):
    global check
    if depth == 3: # depth 3까지 찾아봤는데 거리두기 잘 지키는 경우 True
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <5 and 0<= ny <5 and visited[nx][ny] == 0 and place[nx][ny] != 'X':
            if place[nx][ny] == 'P':
                check = 0
                return
            else:
                visited[nx][ny] = 1
                dfs(place,nx,ny,depth + 1)
                visited[nx][ny] = 0
    return
        

def solution(places):
    global visited
    global check
    answer = []
    for place in places:
        flag = 0
        check = 1 # 거리두기 잘지킴
        visited = [[0] * 5 for _ in range(5)]
        for i in range(5):
            if flag == 1: # 이미 거리두기 안지키는 사람을 발견함
                break
            for j in range(5):
                if place[i][j] == 'P' and not visited[i][j]:
                    visited[i][j] = 1
                    dfs(place,i,j,1)
                    if check:
                        continue
                    else: # 거리두기 안지키는게 발견
                        answer.append(0)
                        flag = 1
                        break
        else:
            answer.append(1)

    return answer
# 3번 풀이
from collections import deque
def bfs(place):
    dx = [0,0,-1,1] # 우좌상하
    dy = [1,-1,0,0]
    start = []
    q = deque()
    visited = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P' and not visited[i][j]:
                start.append((i,j))

    for s in start:
        i,j = s
        visited = [[0] * 5 for _ in range(5)]
        visited[i][j] = 1
        q.append(s)
        while q:
            x, y = q.popleft()
            if visited[x][y] < 3:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 5 and 0<= ny < 5 and place[nx][ny] != 'X' and not visited[nx][ny]:
                        if place[nx][ny] == 'P':
                            return 0
                        else:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx,ny))
    
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    
    return answer
if __name__ == '__main__':
    places = [["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
              ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))