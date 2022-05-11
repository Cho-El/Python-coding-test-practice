import sys

def solution(n,paths,gates, summits):
	print(n,paths,gates,summits)

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
		solution(n,paths,gates,summits)