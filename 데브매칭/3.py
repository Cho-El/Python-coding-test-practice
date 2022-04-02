import sys
sys.setrecursionlimit
answer = 0
def dfs(graph, a, b, k,visited,cnt):
    global answer
    if cnt > k: # cnt가 k를 넘었을 때 return False
        return False
    if cnt <=k and a == k:
        # for i in range(len(visited)):
        #     if visited[i] == 1:
        return True
    
    visited[a] = 1
    for i in graph[a]:
        if not visited[i]:
            if dfs(graph,i,b,k,visited,cnt + 1):
                answer += 1

    return True

def solution(n, edges, k, a, b):
    cnt = 0
    graph = [[] for _ in range(n)]
    visited = [0] * n
    for edge in edges:
        p,q = edge
        graph[p].append(q)
        graph[q].append(p)
    
    print(graph)
    dfs(graph,a,b,k,visited,cnt)
    return answer

edges = [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]]
print(solution(8,edges,4,0,3))