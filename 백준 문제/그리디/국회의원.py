N = int(input())
a = []
for _ in range(N):
	a.append(int(input()))

dasom = a[0]
b = a[1:]
b.sort()
while dasom > max(b):
	
