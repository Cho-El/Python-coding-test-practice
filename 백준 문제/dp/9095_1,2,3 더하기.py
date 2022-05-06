# dp
# 1번 풀이 bfs로 풀어봄
# import sys
# from collections import deque
# t = int(input())

# def bfs():
#     q = deque()
#     q.append([n,''])
#     array = [1,2,3]
#     result = 0
#     visited = set()

#     while q:
#         now,s = q.popleft()
#         if now == 0:
#             result += 1

#         for i in range(3):
#             temp = now - array[i]
#             s = s + str(array[i])
#             if s not in visited and temp >= 0:
#                 q.append([temp,s])
#                 visited.add(s)

#     return result
                

# for _ in range(t):
#     n = int(input())
#     print(bfs())

# 2번 풀이 dp로 풀어보기
import sys
t = int(input())
dp = [0,1,2,4] + [0] * 7
for _ in range(t):
    n = int(input())
    dp = [0,1,2,4] + [0] * 7
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])