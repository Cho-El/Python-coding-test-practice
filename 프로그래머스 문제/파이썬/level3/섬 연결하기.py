def solution1(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    print(costs)
    routes = set([costs[0][0]]) # 집합
    print(routes)
    while len(routes)!=n: # 정점이 다돌았는지 확인
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes: # 둘다 routes안에 있으므로 사이클 형성
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n,costs):
    parent = []
    answer = 0
    cnt = 0
    for i in range(n):
        parent.append(i) # 부모 테이블 초기화
    costs.sort(key = lambda x : x[-1]) # costs 간선 크기로 정렬
    for a, b, w in costs:
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent, a, b)
            answer += w
            cnt += 1
            if cnt == n-1:
                break
    
    return answer
        
            




costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n =4
print(solution(n, costs))

