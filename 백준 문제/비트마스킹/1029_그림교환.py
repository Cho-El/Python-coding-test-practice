# 
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append([int(j) for j in input().rstrip()])

dp = [[[0] * 10 for j in range(1 << n)] for i in range(n)]

def dfs(artist, visited, price):
    
    if dp[artist][visited][price] != 0:
        return dp[artist][visited][price]
    
    if visited == (1 << n) - 1: # 다 방문 되었으면 끝
        return 1
    
    count = 1
    for next_a in range(1, n):
        if graph[artist][next_a] < price or (1 << next_a) & visited > 0:
            continue
        count = max(count, dfs(next_a, (1 << next_a) | visited, graph[artist][next_a]) + 1)
        
    dp[artist][visited][price] = count 

    return count

print(dfs(0,1,0))
    


# import sys
# input = sys.stdin.readline

# def solution(n, arr):
#     M = [[[0] * 10 for j in range(1 << n)] for i in range(n)] # M[artist][path(bin)][price]

#     def dfs(artist, path, price):
#         if M[artist][path][price] != 0: # 메모제이션 적용
#             return M[artist][path][price]

#         count = 0 # 현재 artist 부터의 최대 거래 횟수
#         for nextA in range(1, n):
#             if arr[artist][nextA] < price or path & (1 << nextA) > 0: 
#                 continue
#             count = max(count, 1 + dfs(nextA, path | (1 << nextA), arr[artist][nextA]))
#         M[artist][path][ price] = count # 메모!

#         return count

#     return 1 + dfs(0, 1, 0) 

# if __name__ == '__main__':
#     n = int(input())
#     arr = []
#     for i in range(n):
#         arr.append([int(j) for j in input().strip()])
#     result = solution(n, arr)
#     print(result)