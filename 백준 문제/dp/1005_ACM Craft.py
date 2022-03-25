import sys
from collections import deque

i = 1
t = int(input())
for _ in range(t):
	n, k = map(int, sys.stdin.readline().split())
	graph = [[] for _ in range(n+1)] # i번 노드에서 다음 건물로 갈 수 있는 노드 리스트
	graph_in = [[] for _ in range(n+1)] # i번 노드로 갈 수 있는 노드 리스트

	indegree = [0] * (n + 1)
	dp = [0]
	dp += list(map(int, sys.stdin.readline().split()))
	
	for i in range(k):
		a,b = map(int, sys.stdin.readline().split())
		graph[a].append(b)
		graph_in[b].append(a)
		indegree[b] += 1
	target = int(sys.stdin.readline())

	# dp는 i번 노드까지 걸리는 최소 시간

	def topology_sort():
		q = deque()
		for i in range(1,n+1):
			if indegree[i] == 0:
				q.append(i)
		
		while q:
			now = q.popleft()
			temp = []

			for prev in graph_in[now]:
				temp.append(dp[prev])

			if not temp:
				dp[now] = dp[now]
			else:
				dp[now] = dp[now] + max(temp)

			for next in graph[now]:
				indegree[next] -= 1
				if indegree[next] == 0:
					q.append(next)
	
	topology_sort()
	print(dp[target])
		
