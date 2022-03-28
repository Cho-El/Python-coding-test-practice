import time
# 브루트포스 알고리즘
# 1번 풀이----------------------------------
n = int(input())
num = []
a = time.time()

for i in range(666,2666800):
	if '666' in str(i):
		num.append(i)

num.sort()
b = time.time()
print(num[n-1])
print(b-a)

# 2번 풀이----------------------------------
# n = int(input())
a = time.time()
default = 666
while n != 0:
	if '666' in str(default):
		n -= 1
		answer = default
	default += 1
b = time.time()
print(answer)
print(b-a)
