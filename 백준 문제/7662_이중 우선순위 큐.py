# 트리 힙
import sys
import heapq # 문자열도 받을 수 있음
t = int(input())

for _ in range(t):
    k = int(input())
    max_q = []
    min_q = []
    visited = [0] * k
    for i in range(k):
        s, n = sys.stdin.readline().split()
        if s == 'I':
            heapq.heappush(max_q,(-int(n),i))
            heapq.heappush(min_q,(int(n),i))
            visited[i] = 1
        
        else:
            if n == '-1':
                while min_q and visited[min_q[0][1]] == 0:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = 0
                    heapq.heappop(min_q)

            else:
                while max_q and visited[max_q[0][1]] == 0:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = 0
                    heapq.heappop(max_q)


    while min_q and visited[min_q[0][1]] == 0:
        heapq.heappop(min_q)
    while max_q and visited[max_q[0][1]] == 0:
        heapq.heappop(max_q)

    if not min_q:
        print("EMPTY")
    else:
        print(-1*max_q[0][0], end = ' ')
        print(min_q[0][0])