# 다잌스트라
import sys
import heapq
input = sys.stdin.readline
v,e = map(int, input().rstrip().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
	a,b,c = map(int, input().rstrip().split())
	graph[a].append((b,c))

def dijkstra(start):
	distance = [float('inf')] * (v + 1)
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q:
		dist, node = heapq.heappop(q)
		if distance[node] < dist:
			continue
		for next_node in graph[node]:
			cost = dist + next_node[1]
			if distance[next_node[0]] > cost:
				distance[next_node[0]] = cost
				heapq.heappush(q, (cost, next_node[0]))
	return distance

result = dijkstra(k)
for i in range(1,len(result)):
	if result[i] == float('inf'):
		print('INF')
	else:
		print(result[i])