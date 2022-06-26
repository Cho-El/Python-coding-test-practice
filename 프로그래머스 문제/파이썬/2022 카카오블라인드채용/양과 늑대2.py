import sys
from collections import defaultdict, deque
def dfs(paths, info, graph, s, w):
	global answer

	answer = max(answer, s)
	for i in range(len(paths)):
		node = paths.popleft()
		if info[node] == 0: # 양인 경우
			for j in graph[node]:
				paths.append(j)
			dfs(paths, info, graph, s + 1, w)
			for j in graph[node]:
				paths.pop()

		else: # 늑대인 경우
			if s > w + 1:
				for j in graph[node]:
					paths.append(j)
				dfs(paths, info, graph, s, w + 1)
				for j in graph[node]:
					paths.pop()
					
		paths.append(node)
		

def solution(info, edges):
	global answer
	answer = 0
	graph = defaultdict(list)
	for i in edges:
		graph[i[0]].append(i[1])
	
	path = deque([0])
	dfs(path, info, graph, 0, 0)
	return answer

if __name__ == '__main__':
    inp = [([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]), ([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])]
    for i in inp:
        info, edges = i
        print(solution(info, edges))