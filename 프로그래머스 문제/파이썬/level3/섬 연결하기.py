def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    print(costs)
    routes = set([costs[0][0]]) # 집합
    print(routes)
    while len(routes)!=n: # 정점이 다돌았는지 확인
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans


costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n =4
print(solution(n, costs))