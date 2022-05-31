import sys
from collections import defaultdict
def dfs(path, graph, s, w):
	pass

def solution(info, edges):
	global answer
	answer = 0
	graph = defaultdict(list)
	for i in edges:
		graph[i[0]].append(i[1])
	
    dfs([0],graph, sheep, wolf)
	return answer

if __name__ == '__main__':
    inp = [([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]), ([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])]
    for i in inp:
        info, edges = i
        print(solution(info, edges))