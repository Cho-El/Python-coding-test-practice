import sys
from collections import deque
input = sys.stdin.readline
graph = []
for i in range(8):
    graph.append(list(input().rstrip()))

answer = 0

def bfs():
    direction = [[0,0],[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,-1],[1,1],[-1,1]]
    visited = [[0] * 8 for _ in range(8)]
    dq = deque([7,0,0])
    