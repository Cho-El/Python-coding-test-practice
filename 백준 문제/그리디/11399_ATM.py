import sys

n = int(input())
l = list(map(int, sys.stdin.readline().split()))
answer = []
l.sort()
sum1 = 0
for time in l:
    sum1 += time
    answer.append(sum1)

print(sum(answer))