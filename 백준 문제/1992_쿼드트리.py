# 분할정복 재귀
import sys
def div(x,y,size):
    if check(x,y,size):
        return graph[x][y]
    else:
        size //= 2
        temp = ''
        temp += div(x, y, size)
        temp += div(x, y + size, size)
        temp += div(x + size,y, size)
        temp += div(x + size, y + size, size)
        temp = '(' + temp + ')'
        return temp


def check(x,y,size):
    start = graph[x][y]
    for i in range(x,x + size):
        for j in range(y, y + size):
            if start != graph[i][j]:
                return False
    return True

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

print(div(0,0,n))
