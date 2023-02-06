def solution(n,relation,dirname):
    global result
    result = 0
    graph = [[] for _ in range(n + 1)]
    for root,child in relation:
        graph[root].append(child)
        
    print(graph)
    dfs(1, graph, dirname, 0, 0)
    return result

def dfs(start, graph, dirname, dirLen, depth):
    global result
    dirLen += len(dirname[start-1]) + 1
    if not graph[start]:
        result = max(result, dirLen - 1)
        return
    
    for g in graph[start]:
        dfs(g, graph, dirname, dirLen, depth + 1)
    
        
if __name__ == "__main__":
    print(solution(7,[[1,2],[2,5],[2,6],[1,3],[1,4],[3,7]],["root","abcd","cs","hello","etc","hello","solution"]))