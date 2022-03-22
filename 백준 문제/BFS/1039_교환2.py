import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())

def bfs():
	visited = set()
	q = deque([n])
	size = len(q)
	while size:
		size -= 1
		num = q.popleft()
		n_str = list(str(num))
		for i in range(len(n_str) - 1):
			for j in range(i, len(n_str)):
				if i == 0 and n_str[j] == '0': continue

				n_str[i], n_str[j] = n_str[j], n_str[i]
				real_n = int(''.join(n_str))
				if real_n not in visited:
					visited.add(real_n)
					q.append(real_n)
				n_str[i], n_str[j] = n_str[j], n_str[i]
				
	if not visited:
		return -1

	answer = max(visited)
	return answer


while k:
	k-= 1
	answer = bfs()

print(answer)