import sys
from copy import deepcopy
input = sys.stdin.readline
INF = sys.maxsize
min_cost = INF
n = int(input())
visited = [False] * n
result = []
mp, mf, ms, mv = map(int, input().rstrip().split())

food_info = []
for _ in range(n):
    food_info.append(list(map(int, input().rstrip().split())))

    
def dfs(start, use, nutr):
    global min_cost, result
    visited[start] = True
    use.append(start)
    for i in range(5):
        nutr[i] = food_info[start][i] + nutr[i]
        
    if min_cost < nutr[-1]:
        return 
    
    if nutr[0] >= mp and nutr[1] >= mf and nutr[2] >= ms and nutr[3] >=mv:
        if min_cost > nutr[-1]:
            min_cost = nutr[-1]
            temp = deepcopy(use)
            result = [temp]
        elif min_cost == nutr[-1]:
            temp = deepcopy(use)
            result.append(temp)
        return
    
    for i in range(start + 1, n):
        dfs(i,use, nutr)
        visited[i] = False
        temp = use.pop()
        for i in range(5):
            nutr[i] = nutr[i] - food_info[temp][i]
    
for i in range(n):
    dfs(i, [], [0,0,0,0,0])

if result:
    print(min_cost)
    result.sort()
    for i in result[0]:
        print(i + 1, end = ' ')
else:
    print(-1)
