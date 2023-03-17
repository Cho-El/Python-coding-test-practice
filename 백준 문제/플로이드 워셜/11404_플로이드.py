# 플로이드
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 100000000
graph = [[INF] * (n) for _ in range(n)]

for i in range(m):
    a,b,c = map(int, input().split())
    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c
        
for i in range(n):
    for a in range(n):
        for b in range(n):
            if a != b:
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end = " ")
            continue
        print(graph[i][j], end = " ")
    print()