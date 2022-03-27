import sys
n = int(input())
s = []
for _ in range(n):
	temp = sys.stdin.readline().rstrip()
	if temp not in s:
		s.append(temp)
s.sort()
s.sort(key = len)

for i in s:
	print(i)