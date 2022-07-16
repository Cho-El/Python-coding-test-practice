#
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().rstrip().split())

graph = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
	graph.append(list(map(int, input().rstrip().split())))

def bfs(start):
	