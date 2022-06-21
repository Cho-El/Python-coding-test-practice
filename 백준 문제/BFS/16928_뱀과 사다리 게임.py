# bfs
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())

shortcut = {}
for i in range(n + m):
    x, y = map(int, input().split())
    shortcut[x] = y

visited = [0] * 101

def bfs():
    q = deque([1])
    while q:
        num = q.popleft()
        for i in range(1, 7):
            next_n = num + i
            if 1 <= next_n <= 100 and not visited[next_n] and next_n != 1:
                if next_n in shortcut:
                    next_n = shortcut[next_n]
                if not visited[next_n]:
                    q.append(next_n)
                    visited[next_n] = visited[num] + 1

            
bfs()
print(visited[100])