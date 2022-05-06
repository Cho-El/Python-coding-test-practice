# 분할정복 재귀
import sys
from collections import deque

def div_graph(x,y,size):
    if check(x,y,size):
        result[graph[x][y]] += 1

    else:
        size //= 3
        for i in range(x,x + size*3,size):
            for j in range(y,y + size*3,size):
                if size == 1:
                    result[graph[i][j]] += 1
                else:
                    div_graph(i,j,size)
    

def check(x,y,size):
    start = graph[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if start != graph[i][j]:
                return False
    
    return True

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

result = {-1:0, 0:0, 1:0}
div_graph(0,0,n)
for i in result.values():
    print(i)