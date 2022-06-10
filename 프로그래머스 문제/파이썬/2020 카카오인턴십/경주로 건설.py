# 1번 풀이 60점
import sys
from collections import deque

def bfs(x,y,board):
    q = deque()
    n = len(board)
    q.append((x,y,-1)) # x값 y값 움직이고 있는 방향
    prev_d = -1 # 바뀐 인덱스 해당 인덱스만 계속 바뀐다면 방향 전환은 이러나지 않음
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while q:
        x,y,d = q.popleft()
        for i in range(4):
            if dx[i] != 0:
                direction = 1
            else:
                direction = 0
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < len(board) and 0<= ny < len(board) and board[nx][ny] != 1 and not(nx == 0 and ny == 0):
                if board[nx][ny] != 0 and board[x][y] >= board[nx][ny]: # 다음 칸을 방문한적이 있는데 그 값이 지금 칸에 100을 더한 값보다 큰 경우 pass
                    continue

                # 다음 칸 값 계산------------------------------------------------------
                temp = board[x][y] + 100
                if d != -1 and d != direction: # 첫 시작이 아니고 방향 전환이 일어나는 경우
                    temp += 500
                
                if board[nx][ny] !=0: # nx, ny 번째 칸의 값이 있는 경우
                    board[nx][ny] = min(temp,board[nx][ny])
                    q.append((nx,ny,direction))
                    continue

                board[nx][ny] = temp
                q.append((nx,ny,direction))
    
    return board[n-1][n-1]



def solution(board):
    return bfs(0,0,board)

# 2번 풀이 72점
import sys
from collections import deque

def bfs2(x,y,board):
    q = deque()
    n = len(board)
    q.append((x,y,-1)) # x값 y값 움직이고 있는 방향
    prev_d = -1 # 바뀐 인덱스 해당 인덱스만 계속 바뀐다면 방향 전환은 이러나지 않음
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    while q:
        x,y,d = q.popleft()
        for i in range(4):
            direction = i
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 조건, 벽이 아닐때, nx,ny가 둘다 0이 아닐때
            if 0<= nx < len(board) and 0<= ny < len(board) and board[nx][ny] != 1 and not(nx == 0 and ny == 0):
                temp = board[x][y] + 100
                if d != -1 and d != direction: # 첫 시작이 아니고 방향 전환이 일어나는 경우
                    temp += 500

                if board[nx][ny] != 0 and temp > board[nx][ny]: # 다음 칸을 방문한적이 있는데 그 값이 현재 temp 값보다 작은 경우 pass
                    continue
                
                board[nx][ny] = temp
                q.append((nx,ny,direction))
    
    return board[n-1][n-1]



def solution2(board):
    return bfs2(0,0,board)

# 3번 풀이 96점 시간초과
import sys
from collections import deque

def bfs3(x,y,board):
    INF = sys.maxsize
    q = deque()
    n = len(board)
    q.append((x,y,-1)) # x값 y값 움직이고 있는 방향
    visited = [[[INF] * n for _ in range(n)] for _ in range(4)] # visited[방향][x][y]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(4):
        visited[i][0][0] = 0

    while q:
        x,y,d = q.popleft()
        for i in range(4):
            direction = i
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 조건, 벽이 아닐때
            if 0<= nx < len(board) and 0<= ny < len(board) and board[nx][ny] != 1:
                # cost값 계산
                cost = visited[d][x][y] + 100
                if d != -1 and d != direction:
                    cost += 500

                if visited[direction][nx][ny] < cost:
                    continue
                visited[direction][nx][ny] = cost
                q.append((nx,ny,direction))
    
    answer = visited[0][n-1][n-1]
    for i in range(1,4):
        answer = min(answer,visited[i][n-1][n-1])
    
    return answer


def solution3(board):
    return bfs3(0,0,board)

import sys
import collections

def solution4(board):
    INF=sys.maxsize
    n=len(board)
    answer = INF
    dd=[0, 1, 2, 3]
    dy=[0, 1, 0, -1]
    dx=[1, 0, -1, 0]
    dist=[[[INF for _ in range(len(board[0]))] for _ in range(len(board))] for _ in range(4)]
    q=collections.deque()
    q.append([0, 0, 0, 0])
    q.append([0, 0, 0, 1])
    while q:
        y, x, cost, d=q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<n and board[ny][nx]==0:
                n_cost=cost+1
                if d!=dd[i]:
                    n_cost+=5
                if dist[dd[i]][ny][nx]>n_cost:
                    dist[dd[i]][ny][nx]=n_cost
                    if ny==n-1 and nx==n-1:
                        continue
                    q.append([ny, nx, n_cost, dd[i]])
    for i in range(4):
        answer=min(answer, dist[i][n-1][n-1])
    answer*=100
    return answer

if __name__ == '__main__':
    board = [[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
            [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]],
            [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]],
            [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]]
    for i in board:
        print(solution3 (i))