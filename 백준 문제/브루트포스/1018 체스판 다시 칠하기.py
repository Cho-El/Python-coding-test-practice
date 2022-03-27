import sys
n,m = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
	graph.append(list(sys.stdin.readline().rstrip()))

result = []
start = ['W', 'B']
for i in range(n-7):
	for j in range(m-7):
		temp = []
		for s in range(2):
			cnt = 0
			for x in range(i,i+8):
				for y in range(j,j+8):
					if graph[x][y] == start[s]:
						s = (s + 1)%2
					else:
						s =(s + 1)%2
						cnt += 1
				s = (s + 1)%2
			temp.append(cnt)
		result.append(min(temp))

print(min(result))

'''
브루트 포스
a[x][y] 배열에서
체스의 검은판만 검사하는 방법
첫 시작이 검은색일 때
(x + y) % 2 ==0
'''