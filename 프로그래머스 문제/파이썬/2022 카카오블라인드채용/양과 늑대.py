# from collections import defaultdict, deque  #
# from copy import deepcopy
 
# is_wolf = list()
# num2edges = defaultdict(list)
# max_sheep = 0

    
# def find_max_recursive(current_loc, used, nsheep, nwolf, can_go): # 최대 양의 수 찾기
#     global max_sheep

#     if used[current_loc] : # 이미 데려온적 있으면
#         return
#     used[current_loc] = True

#     if is_wolf[current_loc]: # 
#         nwolf += 1
#     else:
#         nsheep += 1
#         max_sheep = max(max_sheep, nsheep)

#     if nsheep <= nwolf:
#         return
    
#     can_go.extend(num2edges[current_loc])
#     for next_loc in can_go:
#         find_max_recursive(next_loc, deepcopy(used), nsheep, nwolf,
#                             can_go = [loc for loc in can_go if loc != next_loc and not used[loc]])

# def solution(info, edges):
#     global is_wolf, num2edges, max_sheep
#     is_wolf = info # 전역변수에 할당
#     used = [False] * len(is_wolf) # 방문한 노드 확인 용 변수
 
#     for e_from, e_to in edges:
#         num2edges[e_from].append(e_to) # 연결된 엣지 리스트에 추가

#     find_max_recursive(0, used, 0, 0, [])
#     return max_sheep




# 현재 위치에서 갈 수 있는 노드 찾기
def getCanGoEdges(i, prev, graph):
    canGoEdges = [edge for edge in prev if edge != i]
    for j in range(len(graph)):
        if graph[i][j] == True:
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

if __name__ == '__main__':
    inp = [([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]), ([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]])]
    for i in inp:
        info, edges = i
        print(solution(info, edges))