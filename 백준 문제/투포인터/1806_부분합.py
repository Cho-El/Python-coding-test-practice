# 투포인터
import sys
input = sys.stdin.readline
INF = sys.maxsize

N,S = map(int, input().split())
graph = list(map(int, input().split()))
result = INF
end = 0
tempSum = 0

for start in range(N):
    while end < N and tempSum < S:
        tempSum += graph[end]
        end += 1
        
    if tempSum >= S:
        result = min(result, end - start)
    tempSum -= graph[start]

if result == INF:
    print(0)
else:
    print(result)