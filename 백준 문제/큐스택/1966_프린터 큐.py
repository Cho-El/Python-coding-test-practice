import sys
from collections import deque
# 구현 자료구조 시뮬레이션 큐
t = int(input())
for _ in range(t):
    result = 0
    q = deque()
    n,m = map(int,sys.stdin.readline().split())
    temp = list(map(int,sys.stdin.readline().split()))
    for ix, v in enumerate(temp):
        q.append((ix,v))

    while q:
        index, value = q.popleft()
        if q and value < max(q, key = lambda x : x[1])[1]: # 뒤로 빼기
            q.append((index, value))

        else:
            result += 1
            if index == m:
                break
    
    print(result)