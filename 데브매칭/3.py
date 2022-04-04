import sys
sys.setrecursionlimit
answer = 0
result = set()
def dfs(graph, a, b, k,visited,cnt,edge_t):
    global answer
    if cnt > k: # cnt가 k를 넘었을 때 return False
        return
    if cnt <=k and a == b:
        result.update(edge_t)
        return
    
    visited[a] = 1
    for i in graph[a]:
        if not visited[i]:
            x, y = sorted((a,i))
            edge_t.append((x,y))
            dfs(graph,i,b,k,visited,cnt + 1,edge_t)
            edge_t.pop()
            visited[i] = 0
    return

def solution(n, edges, k, a, b):
    cnt = 0
    graph = [[] for _ in range(n)]
    visited = [0] * n
    for edge in edges:
        p,q = edge
        graph[p].append(q)
        graph[q].append(p)

    
    edge_t = []
    dfs(graph,a,b,k,visited,cnt,edge_t)

    return len(edges)-len(result)

edges = [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]]
print(solution(8,edges,4,0,3))