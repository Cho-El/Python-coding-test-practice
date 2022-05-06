# 플로이드 워셜
import sys
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for k in range(0, n):
    for a in range(0, n):
        for b in range(0, n):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

for i in graph:
    for j in i:
        print(j, end = ' ')
    print()
