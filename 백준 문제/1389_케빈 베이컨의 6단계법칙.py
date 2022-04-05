import sys
from collections import deque
sys.setrecursionlimit
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n + 1)

for _ in range(m):
	a,b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

def bfs(start):
	q = deque([start])
	visited[start] = 0
	while q:
		now = q.popleft()
		for i in graph[now]:
			if visited[i] == -1:
				visited[i] = visited[now] + 1
				q.append(i)
	
	return sum(visited[1:])



def solution(n,m):
	global visited
	result = []
	for i in range(1,n):
		result.append((i,bfs(i)))
		visited = [-1] * (n + 1)
	result.sort(key = lambda x : x[1])
	print(result[0][0])

solution(n,m)