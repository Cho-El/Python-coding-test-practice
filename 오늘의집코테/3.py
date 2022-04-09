'''
순환 체크
{} 안에 값 찾는 함수

'''
from collections import defaultdict
visited = {}
graph = {}
def dfs(start,familly): #
    visited[start] = 1
    familly.append(start)
    next = graph[start]

    if visited[next] == 0:
        dfs(next,familly)
    elif visited[next] == -1:
        last_value = graph[next]
        for f in familly:
            graph[f] = last_value
        return

    else: # 순회
        for f in familly:
            graph[f] = '{' + f'{f}' + '}'
        return 


def solution(tstring, variables):
    # 순환 체크
    start = []
    global visited, graph
    for va in variables:
        if va[1][-1] == '}' and va[1][0] == '{':
            visited[va[0]] = 0
            graph[va[0]] = va[1].strip('}{')
            
        else:
            visited[va[0]] = -1
            graph[va[0]] = va[1]
    print(graph)

    # 시작점 찾기
    for k,v in graph.items():
        if visited[k] == 0 and k not in graph.values():
            start.append(k)
    print(start)

    for st in start: # 시작점이 있는 값들 다 돌리기
        temp = []
        dfs(st,temp)

    for k,v in graph.items():
        if visited[k] == 0:
            temp = []
            dfs(k,temp)
    print(graph)

    # 문장 바꾸기
    for g in graph:
        target = '{' + g + '}'
        if target in tstring:
            tstring = tstring.replace(target, graph[g]).rstrip()
    
    print(tstring)
    return

tstring = "this is {template} {template} is {state}"
variables = [["template", "{state}"], ["state", "{templates}"]]
solution(tstring, variables)