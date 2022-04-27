#
import sys

def solution(n,s,a):
	for i in range(n-1):
		if s==0:
			break
		mx, idx=a[i], i
		for j in range(i+1, min(n, i+1+s)):
			if mx<a[j]:
				mx=a[j]
				idx=j
		s-=idx-i
		for j in range(idx, i, -1):
			a[j]=a[j-1]
		a[i]=mx
	print(*a)

if __name__ == '__main__':
	n = int(input())
	array = list(map(int, sys.stdin.readline().split()))
	s = int(input())
	solution(n,s,array)