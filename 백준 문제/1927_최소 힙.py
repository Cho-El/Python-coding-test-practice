# 우선순위 큐 자료구조
import sys
import heapq
n = int(input())
q = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x > 0 :
        heapq.heappush(q, x)
    else:
        if q:
            t = heapq.heappop(q)
            print(t)
        else:
            print(0)