import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
def dfs(start,gates,intensity, summits):
	global graph, visited, final_intensity
	visited[start] = True
	if start in gates: # 출입구에 다다르면 종료
		final_intensity.append(intensity)
		return

	for i in graph[start]:
		next_node, cost = i
		if not visited[next_node] and next_node not in summits:
			visited[next_node] = True
			temp = intensity
			intensity = max(intensity, cost)
			dfs(next_node, gates, intensity, summits)
			# 초기화
			intensity = temp
			visited[next_node] = False
	
	return 

			

def solution1(n,paths,gates, summits):
	global graph, visited, final_intensity
	graph = [[] for _ in range(n + 1)]
	visited = [False for _ in range(n + 1)]
	intensity_list = []
	for path in paths:
		x, y, cost = path
		graph[x].append((y,cost))
		graph[y].append((x,cost))
	
	# 산봉오리에서 시작 dfs gates에 도착하면 끝
	for summit in summits:
		final_intensity = []
		dfs(summit, gates,0, summits)
		intensity_list.append([summit, min(final_intensity)])
	
	intensity_list.sort(key = lambda x : x[::-1])
	return intensity_list[0]

import sys, heapq
from collections import defaultdict
def dijkstra(intensity, graph, summitCheck, gates):
    q = []
    for gate in gates:
        heapq.heappush(q, (0, gate))
    
    while q:
        weight, now = heapq.heappop(q)
        # continue 조건 : 정상에 도착하거나 현재 
        if now in summitCheck or weight > intensity[now]:
            continue
        
        for next in graph[now]:
            nextNode, nextWeight = next
            cost = max(nextWeight, weight)
            if cost < intensity[nextNode]:
                intensity[nextNode] = cost
                heapq.heappush(q, (cost, nextNode))
    
def solution(n,paths,gates, summits):
    inf = sys.maxsize
    graph = defaultdict(list)
    intensity = [inf for _ in range(n + 1)]
    summitCheck = set(summits)
    answer = []
    for path in paths:
        a,b,weight = path
        graph[a].append((b,weight))
        graph[b].append((a, weight))
    
    dijkstra(intensity, graph, summitCheck, gates)
    
    for summit in summits:
        answer.append([summit, intensity[summit]])
    
    answer.sort(key = lambda x : [x[1], x[0]])
    return answer[0]

print(solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
               [1,3],
               [5]))