# 분할정복, 재귀
import sys

def div(x,y,size):
    if check(x,y,size):
        result[graph[x][y]] += 1
    else:
        size //= 2
        div(x,y,size)
        div(x, y + size, size)
        div(x + size, y, size)
        div(x + size, y + size, size)



def check(x,y,size):
    start = graph[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if start != graph[i][j]:
                return False
    return True

graph = []
result = [0,0] # 흰색0이 result[0], 파란색1이 result[1]
n = int(input())
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

div(0,0,n)
for i in result:
    print(i)