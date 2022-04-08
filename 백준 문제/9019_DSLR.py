#
# 1번 풀이 시간초과
# import sys
# from collections import deque
# t = int(input())
# def D(n):
# 	n = int(''.join(n))
# 	n *= 2
# 	if n >= 10000:
# 		n %= 10000
# 	return n
	
# def S(n):
# 	n = int(''.join(n))
# 	n -= 1
# 	if n < 0:
# 		n = 9999
# 	return n

# def L(n):
# 	for i in range(len(n)-1):
# 		n[i], n[i-1] = n[i-1], n[i] 
# 	return int(''.join(n))

# def R(n):
# 	for i in range(len(n)-1,0,-1):
# 		n[i], n[(i+1) % len(n)] = n[(i+1) % len(n)], n[i]
# 	return int(''.join(n))

# def bfs():
# 	q = deque([start])
# 	t = int(''.join(target))

# 	while visited[t] == '':
# 		now = q.popleft()
# 		now_n = int(''.join(now))
# 		d = D(now)
# 		s = S(now)
# 		l = L(now)
# 		r = R(now)
# 		if visited[d] == '':
# 			visited[d] = visited[now_n] + 'D'
# 			q.append(list(str(d)))
# 		if visited[s] == '':
# 			visited[s] = visited[now_n] + 'S'
# 			q.append(list(str(s)))
# 		if visited[l] == '':
# 			visited[l] = visited[now_n] + 'L'
# 			q.append(list(str(l)))
# 		if visited[r] == '':
# 			visited[r] = visited[now_n] + 'R'
# 			q.append(list(str(r)))
		


# for _ in range(t):
# 	start, target = map(list,sys.stdin.readline().split())
# 	visited = [''] * 10000
# 	bfs()
# 	t = int(''.join(target))
# 	print(visited[t])

# 2번 풀이
# import sys
# from collections import deque
# t = int(input())
# def J(list):
# 	return int(''.join(list))

# def D(n):
# 	n = int(n)
# 	n *= 2
# 	if n >= 10000:
# 		n %= 10000
# 	return n
	
# def S(n):
# 	n = int(n)
# 	n -= 1
# 	if n < 0:
# 		n = 9999
# 	return n

# def L(n):
# 	n = list(n)
# 	for i in range(len(n)-1):
# 		n[i], n[i-1] = n[i-1], n[i] 
# 	return J(n)

# def R(n):
# 	n = list(n)
# 	for i in range(len(n)-1,0,-1):
# 		n[i], n[(i+1) % len(n)] = n[(i+1) % len(n)], n[i]
# 	return J(n)

# def bfs():
# 	q = deque([start])
# 	t = int(target)

# 	while visited[t] == '':
# 		now = q.popleft() # '1234'
# 		now_n = int(now)
# 		d = D(now)
# 		s = S(now)
# 		l = L(now)
# 		r = R(now)

# 		if visited[d] == '':
# 			visited[d] = visited[now_n] + 'D'
# 			q.append(str(d))
# 		if visited[s] == '':
# 			visited[s] = visited[now_n] + 'S'
# 			q.append(str(s))
# 		if visited[l] == '':
# 			visited[l] = visited[now_n] + 'L'
# 			q.append(str(l))
# 		if visited[r] == '':
# 			visited[r] = visited[now_n] + 'R'
# 			q.append(str(r))
		


# for _ in range(t):
# 	start, target = sys.stdin.readline().split()
# 	visited = [''] * 10000
# 	bfs()
# 	t = int(target)
# 	print(visited[t])

# 3번 풀이
# import sys
# from collections import deque
# t = int(input())

# def D(n):
# 	n *= 2
# 	if n >= 10000:
# 		n %= 10000
# 	return n
	
# def S(n):
# 	n -= 1
# 	if n < 0:
# 		n = 9999
# 	return n

# def L(n):
# 	return (n % 1000) * 10 + n // 1000

# def R(n):
# 	return (n % 10) * 1000 + n // 10

# def bfs():
# 	q = deque([start])

# 	while q:
# 		now = q.popleft()
# 		d = D(now)
# 		s = S(now)
# 		l = L(now)
# 		r = R(now)
# 		if d == target:
# 			return visited[now] + 'D'
# 		if s == target:
# 			return visited[now] + 'S'
# 		if l == target:
# 			return visited[now] + 'L'
# 		if r == target:
# 			return visited[now] + 'R'
		
# 		if visited[d] == '':
# 			visited[d] = visited[now] + 'D'
# 			q.append(d)
# 		if visited[s] == '':
# 			visited[s] = visited[now] + 'S'
# 			q.append(s)
# 		if visited[l] == '':
# 			visited[l] = visited[now] + 'L'
# 			q.append(l)
# 		if visited[r] == '':
# 			visited[r] = visited[now] + 'R'
# 			q.append(r)
		


# for _ in range(t):
# 	start, target = map(int, sys.stdin.readline().split())
# 	visited = [''] * 10000
# 	print(bfs())

# 4번 풀이
import sys
from collections import deque
t = int(input())

def D(n):
	n *= 2
	if n >= 10000:
		n %= 10000
	return n
	
def S(n):
	n -= 1
	if n < 0:
		n = 9999
	return n

def L(n):
	return (n % 1000) * 10 + n // 1000

def R(n):
	return (n % 10) * 1000 + n // 10

def bfs():
	q = deque()
	q.append([start,''])

	while q:
		now, result = q.popleft()
		d = D(now)
		s = S(now)
		l = L(now)
		r = R(now)
		
		if d == target: return result + 'D'
		elif visited[d] == 0:
			visited[d] = 1
			q.append([d, result + 'D'])
		
		if s == target: return result + 'S'
		elif visited[s] == 0:
			visited[s] = 1
			q.append([s, result + 'S'])

		if l == target: return result + 'L'
		elif visited[l] == 0:
			visited[l] = 1
			q.append([l, result + 'L'])

		if r == target: return result + 'R'
		elif visited[r] == 0:
			visited[r] = 1
			q.append([r, result + 'R'])
		


for _ in range(t):
	start, target = map(int, sys.stdin.readline().split())
	visited = [0] * 10000
	print(bfs())