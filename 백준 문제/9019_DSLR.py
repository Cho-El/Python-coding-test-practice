#
import sys
from collections import deque
t = int(input())
def D(n):
	n = int(''.join(n))
	n *= 2
	if n >= 10000:
		n %= 10000
	return n
	
def S(n):
	n = int(''.join(n))
	n -= 1
	if n < 0:
		n = 9999
	return n

def L(n):
	for i in range(len(n)-1):
		n[i], n[i-1] = n[i-1], n[i] 
	return int(''.join(n))

def R(n):
	for i in range(len(n)-1,0,-1):
		n[i], n[(i+1) % len(n)] = n[(i+1) % len(n)], n[i]
	return int(''.join(n))

def bfs():
	q = deque([start])
	t = int(''.join(target))

	while visited[t] == '':
		now = q.popleft()
		now_n = int(''.join(now))
		d = D(now)
		s = S(now)
		l = L(now)
		r = R(now)
		if visited[d] == '':
			visited[d] = visited[now_n] + 'D'
			q.append(list(str(d)))
		if visited[s] == '':
			visited[s] = visited[now_n] + 'S'
			q.append(list(str(s)))
		if visited[l] == '':
			visited[l] = visited[now_n] + 'L'
			q.append(list(str(l)))
		if visited[r] == '':
			visited[r] = visited[now_n] + 'R'
			q.append(list(str(r)))
		


for _ in range(t):
	start, target = map(list,sys.stdin.readline().split())
	visited = [''] * 10000
	bfs()
	t = int(''.join(target))
	print(visited[t])