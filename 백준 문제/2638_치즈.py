#
# import sys
# from collections import deque
# input = sys.stdin.readline
# n,m = map(int, input().rstrip().split())

# graph = []
# visited = [[False] * m for _ in range(n)]
# for _ in range(n):
# 	graph.append(list(map(int, input().rstrip().split())))

# def bfs(start):

import sys
from collections import deque

# 위 - 오 - 아래 - 왼 순서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

H, W = map(int, sys.stdin.readline().split(" "))
field = []

for _ in range(H):
    field.append(list(map(int, sys.stdin.readline().split(" "))))

left = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == 1:
            left += 1

def bfs(left):
    while queue:
        now = queue.popleft()

        for i in range(4):
            ndr = now[0] + dr[i]
            ndc = now[1] + dc[i]

            if 0 <= ndr < H and 0 <= ndc < W and visited[ndr][ndc] == 0:
                visited[ndr][ndc] = 1

                # 치즈 가장자리를 만나면
                if field[ndr][ndc] == 1:
                    field[ndr][ndc] = 2
                    left -= 1
                else:
                    queue.append([ndr, ndc])

    return left


def delete():
    for i in range(H):
        for j in range(W):
            if field[i][j] == 2:
                field[i][j] = 0

queue = deque()

count = 0
temp = left
while left != 0:
    visited = [[0 for _ in range(W)] for _ in range(H)]
    queue.append([0, 0])
    visited[0][0] = 1
    left = bfs(left)

    if left != 0:
        temp = left

    count += 1
    for i in field:
        print(i)
        
    delete()

print(count)
print(temp)