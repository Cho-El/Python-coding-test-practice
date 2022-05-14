
# 현재 위치에서 갈 수 있는 노드 찾기
def getCanGoEdges(i, prev, graph):
    canGoEdges = [edge for edge in prev if edge != i] # 현재 i노드까지의 경로 담기
    for j in range(len(graph)):
        if graph[i][j] == True: # i노드와 연결된 노드 찾기
            canGoEdges.append(j)
    return canGoEdges

# 현재 위치(i) 기준으로 갈 수 있는 곳 가보기 -> DFS
def DFS(i, s, w, prev, graph, info):
    global answer
    canGoEdges = getCanGoEdges(i, prev, graph)
    if s == w or not canGoEdges:
        if answer < s:
            answer = s
        return
    for edge in canGoEdges:
        if info[edge] == 0: # 가려는 노드에 양이 있는 경우
            DFS(edge, s + 1, w, canGoEdges, graph, info)
        else: # 가려는 노드에 늑대가 있는 경우
            DFS(edge, s, w + 1, canGoEdges, graph, info)

def solution(info, edges):
    global answer
    answer = 1
    graph = [[False] * len(info) for _ in range(len(info))]
    for x, y in edges:
        graph[x][y] = True
    DFS(0, 1, 0, [0], graph, info)
    return answer

# from collections import defaultdict
# from collections import deque
# def dfs(dq,scnt,wcnt):
#     global answer
#     answer = max(scnt,answer)
#     for i in range(len(dq)):
#         p = dq.popleft()
#         if infos[p] == 1: # 해당 노드가 늑대일 경우
#             if scnt>wcnt+1: # 양이 더 많은 경우 
#                 for j in D[p]: # 해당 노드의 자식들을 dq에 담음
#                     dq.append(j)
#                 dfs(dq,scnt,wcnt+1)
#                 for j in D[p]:
#                     dq.pop()
#         else: # 해당 노드가 양인 경우
#             for j in D[p]:
#                 dq.append(j)
#             dfs(dq,scnt+1,wcnt)
#             for j in D[p]:
#                 dq.pop()
#         dq.append(p)
    
# def solution(info, edges):
#     global answer,infos,D
#     infos = info # 양, 늑대 여부
#     answer = 0
#     D = defaultdict(list) # 그래프
#     dq = deque()
#     for i in edges:
#         D[i[0]].append(i[1])
#     dq.append(0)
#     dfs(dq,0,0)
#     return answer

if __name__ == '__main__':
    inp = [([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]), ([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])]
    for i in inp:
        info, edges = i
        print(solution(info, edges))