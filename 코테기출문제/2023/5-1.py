# bfs
from collections import deque

# def solution(topping, tasting):
#     q = deque([[0,0,0]]) # start = (0,0,0) -> (지금 지점, 움직인 거리, 찾아야 하는 토핑 인덱스)
    
#     dx = [1,-1]
#     while q:
#         curIdx, dist, targetIdx = q.popleft()
#         # 움직이다가 원하는 토핑을 찾는 경우
#         if topping[curIdx] == tasting[targetIdx]:
#             targetIdx += 1
#             # 다 찾은 경우 바로 리턴후 지금까지의 거리를 출력
#             if targetIdx == len(tasting):
#                 return dist
        
#         # 좌우로 움직이기
#         for i in range(2):
#             nextIdx = curIdx + dx[i]
#             if nextIdx < 0:
#                 nextIdx = len(topping) - 1
#             nextIdx %= len(topping)
#             q.append([nextIdx, dist + 1, targetIdx])

# def bfs(topping, tasting, start):
#     q = deque([start]) # start = (0,0,0) -> (지금 지점, 움직인 거리, 찾아야 하는 토핑 인덱스)
#     dx = [1,-1]
#     while q:
#         curIdx, dist, targetIdx = q.popleft()
#         # 움직이다가 원하는 토핑을 찾는 경우
#         if topping[curIdx] == tasting[targetIdx]:
#             targetIdx += 1
#             # 다 찾은 경우 바로 리턴후 지금까지의 거리를 출력
#             if targetIdx == len(tasting):
#                 return dist
        
#         # 좌우로 움직이기
#         for i in range(2):
#             nextIdx = curIdx + dx[i]
#             if nextIdx < 0:
#                 nextIdx = len(topping) - 1
#             nextIdx %= len(topping)
#             q.append([nextIdx, dist + 1, targetIdx]) 

# def solution(topping, tasting):
#     q = deque([0,0,0]) # [curIdx, dist, nextTargetIdx]
#     while q:
#         curIdx, dist, targetIdx = q.popleft()
#         findIdx = []
#         for i in range(len(topping)):
#             if topping[i] == tasting[targetIdx]:
#                 findIdx.append(i)
        
#         findFirstIdx, findSecondIdx = findIdx[0], findIdx[1]
#         findFirstIdxdist = min(curIdx + len(topping) - findFirstIdx, findFirstIdx)
#         findSecondIdxdist = min(curIdx + len(topping) - findSecondIdx, findSecondIdx)
#         if targetIdx == len(tasting):
#             dist = dist + findFirstIdx
#         q.append([findFirstIdx, findFirstIdxdist, targetIdx + 1])
#         q.append([findSecondIdx, findSecondIdxdist, targetIdx + 1])
                
#     # 왼쪽으로만 이동
    
#     # 오른쪽으로만 이동
    
#     return
def solution(toppings, tasting):
    n = len(toppings)

    # Find positions of each topping on the pizza
    positions = {}
    for i in range(n):
        if toppings[i] not in positions:
            positions[toppings[i]] = []
        positions[toppings[i]].append(i + 1)

    # Helper function to calculate the minimum distance between two positions considering wrap-around
    def min_distance(a, b, n):
        return min(abs(a - b), n - abs(a - b))

    def find_min_time(current_position, tasting_index):
        # 종료 조건
        if tasting_index == len(tasting):
            return 0
        
        topping = tasting[tasting_index]
        pos1, pos2 = positions[topping]
        dist1 = min_distance(current_position, pos1, n) + find_min_time(pos1, tasting_index + 1)
        dist2 = min_distance(current_position, pos2, n) + find_min_time(pos2, tasting_index + 1)

        return min(dist1, dist2)

    return find_min_time(1, 0)

print(solution([2,1,3,1,2,4,4,3], [1,2,3,4]))
print(solution([2,1,3,1,2,4,4,3], [3,1,2,4]))
    