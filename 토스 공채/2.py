from collections import defaultdict
def solution(relationships, target, limit):
    graph = defaultdict(set)
    newFriends = set()
    originalFriends = []
    for relationship in relationships:
        a,b = relationship
        graph[a].add(b)
        graph[b].add(a)
    
    # 원래 친구 계산
    for i in graph[target]:
        originalFriends.append(i)
        
    dfs(0, newFriends, graph, target, limit, originalFriends, [])
    print(originalFriends)
    print(newFriends)
    # 보상 계산
    return 5 * len(originalFriends) + 10 *len(newFriends) + len(newFriends)

def dfs(depth, newFriends, graph, target, limit, originalFriends, visited):
    if depth == limit:
        return
    
    visited.append(target)
    
    for friend in graph[target]:
        # 체크한 친구가 아니라면
        if friend not in visited:
            # 원래 친구라면 depth만 늘려주고 dfs
            if depth == 0 or friend in originalFriends:
                dfs(depth + 1, newFriends, graph, friend, limit, originalFriends, visited)
            # 원래 친구가 아니라면 newFriends에 추가
            else:
                newFriends.add(friend)
                dfs(depth + 1, newFriends, graph, friend, limit, originalFriends, visited)
    
    visited.pop()
                
print(solution([[1,2],[2,3],[2,6],[3,4],[4,5]], 2, 3))