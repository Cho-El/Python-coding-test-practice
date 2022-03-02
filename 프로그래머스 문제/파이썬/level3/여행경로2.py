from collections import defaultdict
def dfs(graph, N, key, footprint):
    if len(footprint) == N + 1:
        return footprint
    
    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret



def solution(tickets):
    graph = defaultdict(list)
    for a,b in tickets:
        graph[a].append(b)
        graph[a].sort()
    
    dfs(graph, len(tickets), "ICN", ["ICN"])
