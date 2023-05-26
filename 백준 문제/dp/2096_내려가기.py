# 첫 풀이
# import sys
# from copy import deepcopy
# input = sys.stdin.readline
# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().rstrip().split())))

# max_score = deepcopy(graph)
# min_score = deepcopy(graph)
# for i in range(n-1):
#     max_score[i + 1][0] = max(max_score[i][0], max_score[i][1]) + max_score[i + 1][0]
#     min_score[i + 1][0] = min(min_score[i][0], min_score[i][1]) + min_score[i + 1][0]
#     max_score[i + 1][1] = max(max_score[i]) + max_score[i + 1][1]
#     min_score[i + 1][1] = min(min_score[i]) + min_score[i + 1][1]
    
#     max_score[i + 1][2] = max(max_score[i][2], max_score[i][1]) + max_score[i + 1][2]
#     min_score[i + 1][2] = min(min_score[i][2], min_score[i][1]) + min_score[i + 1][2]

# print(max(max_score[n - 1]), min(min_score[n - 1]), end = ' ')

# 두번째 풀이
import sys
from copy import deepcopy
input = sys.stdin.readline
n = int(input())
graph = []

max_score = [0] * 3
min_score = [0] * 3

for _ in range(n):
	a,b,c = map(int, input().rstrip().split())
	tmp = deepcopy(max_score)
	max_score[0] = max(tmp[0], tmp[1]) + a
	max_score[1] = max(tmp) + b
	max_score[2] = max(tmp[1], tmp[2]) + c

	tmp = deepcopy(min_score)
	min_score[0] = min(tmp[0], tmp[1]) + a
	min_score[1] = min(tmp) + b
	min_score[2] = min(tmp[1], tmp[2]) + c

	
print(max(max_score), min(min_score))