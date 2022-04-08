#
import sys
t = int(input())
def D(n):
	n = int(''.join(n))
	n *= 2
	if n >= 10000:
		n %= 10000
	return list(str(n))
	
def S(n):
	n = int(''.join(n))
	n -= 1
	if n < 0:
		n = 9999
	return list(str(n))

def L(n):
	for i in range(len(n)-1):
		n[i], n[i-1] = n[i-1], n[i] 
	return n

def R(n):
	for i in range(len(n)-1,0,-1):
		n[i], n[(i+1) % (len(n)-1)] = n[(i+1) % (len(n)-1)], n[i]




for _ in range(t):
	start, target = map(list,sys.stdin.readline().split())
