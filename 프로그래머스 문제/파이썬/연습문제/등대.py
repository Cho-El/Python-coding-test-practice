from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, lighthouse):
    graph = defaultdict(list)
    visited = [False] * (n + 1)
    for l in lighthouse:
        start, end = l
        graph[start].append(end)
        graph[end].append(start)
    
    on, off = dfs(1, graph, visited)
    return min(on, off)

def dfs(n, graph, visited):
    visited[n] = True
    
    on, off = 1, 0
    for nextNode in graph[n]:
        if not visited[nextNode]:
            childOn, childOff = dfs(nextNode,graph,visited)
            on += min(childOn, childOff)
            off += childOn
            
    return on, off
            
 

print(solution(10,[[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))
print(solution(8,[[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))