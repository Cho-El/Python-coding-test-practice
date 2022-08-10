import sys

input = sys.stdin.readline
graph = []
for i in range(8):
    graph.append(list(input().rstrip()))

for i in graph:
    print(i)