# 수학 분할정복을 통한 거듭제곱
import sys
input = sys.stdin.readline

a,b,c = map(int, input().rstrip().split())
def div_mult(a,b,c):
	if b == 1:
		return a % c
	elif b % 2 == 0:
		tmp = div_mult(a, b//2, c)
		return (tmp * tmp) % c
	else:
		tmp = div_mult(a, b//2, c)
		return (tmp * tmp * a) % c

print(div_mult(a,b,c))