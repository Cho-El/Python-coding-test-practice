import sys
from collections import defaultdict
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

			

def solution(n,paths,gates, summits):
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
	
	

if __name__ == '__main__':
	n = [6,7,7,5]
	paths = [[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
	]
	gates = [[1,3], [1], [3,7], [1,2]]
	summits = [[5],[2,3,4],[1,5],[5]]
	for n,paths,gates,summits in zip(n, paths, gates, summits):
		print(solution(n,paths,gates,summits))