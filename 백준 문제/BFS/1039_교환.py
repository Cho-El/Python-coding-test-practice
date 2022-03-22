import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
visited = [set() for _ in range(k)]

def bfs():
    q = deque([n])
    depth = 0
    while q:
        crit = q.popleft()
        n_str = list(str(crit))
        for i in range(len(n_str)-1):
            for j in range(i+1,len(n_str)):
                if i == 0 and n_str[j] == '0':
                    continue
                n_str[i], n_str[j] = n_str[j], n_str[i]
                n_num = int(''.join(n_str))
                if n_num not in visited[depth]:
                    visited[depth].add(n_num)
                n_str[i], n_str[j] = n_str[j], n_str[i]

        if not visited[depth]:
            return -1

        answer = max(visited[depth])
        depth += 1
        q.append(answer)
        if k == depth:
            return answer

result = bfs()
print(result)
