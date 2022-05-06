# 브루트포스
import sys

n = int(input())
m = int(input())

if m :
	breakdown = list(input().split())
else:
	breakdown =[]
answer = abs(100 - n)

for num in range(1000001):
	for i in str(num):
		if i in breakdown:
			break
	else: # for else 문
		answer = min(answer, len(str(num)) + abs(num - n))

print(answer)
