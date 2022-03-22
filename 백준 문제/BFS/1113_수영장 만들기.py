import sys
n,m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
	graph.append(list(map(int, sys.stdin.readline().rstrip())))

