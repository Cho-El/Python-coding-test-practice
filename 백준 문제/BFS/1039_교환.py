import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
visited = [set() for _ in range(k+1)]

# 첫번째 풀이 bfs 한번만 사용
def bfs():
    q = deque([(n,0)])
    depth = 0
    while q:
        crit, depth = q.popleft()
        n_str = list(str(crit))
        if k == depth:
            return(max(visited[depth]))

        for i in range(len(n_str)-1):
            for j in range(i+1,len(n_str)):
                if i == 0 and n_str[j] == '0':
                    continue
                n_str[i], n_str[j] = n_str[j], n_str[i]
                n_num = int(''.join(n_str))
                if n_num not in visited[depth+1]:
                    visited[depth+1].add(n_num)
                    q.append((n_num, depth + 1))
                n_str[i], n_str[j] = n_str[j], n_str[i]

    return -1    

result = bfs()
print(result)
