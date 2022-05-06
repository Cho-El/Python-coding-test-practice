# 자료구조, 문자열, 정렬, 해시
import sys
n,m = map(int, input().split())
no_listen = {}
no_see = []
d = []
for _ in range(n):
    no_listen[sys.stdin.readline().rstrip()] = 1

for _ in range(m):
    see = sys.stdin.readline().rstrip()
    if see in no_listen:
        d.append(see)

d.sort()
print(len(d))
for i in d:
    print(i)