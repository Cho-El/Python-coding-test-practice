# 주의점 v1 v2를 갔다가 최종 목적지를 가는 경우와 v2 v1을 갔다가 최종 목적지를 가는 두가지경우를 생각해야한다.
# 다잌스트라
import sys
import heapq
input = sys.stdin.readline
n,e = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(e):
	a,b,c = map(int, input().rstrip().split())
	graph[a].append((b,c))
	graph[b].append((a,c))

v1,v2 = map(int, input().rstrip().split())

def dijkstra(start, target):
	distance = [float('inf')] * (n + 1)
	q = []
	heapq.heappush(q, (0,start))
	distance[start] = 0
	
	while q:
		dist, node = heapq.heappop(q)
		if distance[node] < dist:
			continue
		for i in graph[node]:
			cost = dist + i[1]
			if distance[i[0]] > cost:
				distance[i[0]] = cost
				heapq.heappush(q, (cost,i[0]))
	
	return distance[target]
result = []

result.append(dijkstra(1,v1) + dijkstra(v1, v2) + dijkstra(v2, n))
result.append(dijkstra(1,v2) + dijkstra(v2, v1) + dijkstra(v1, n))

if min(result) != float('inf'):
	print(min(result))
else:
	print(-1)