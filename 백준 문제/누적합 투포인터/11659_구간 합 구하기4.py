# 누적 합
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
array = list(map(int, input().split()))
prefix_sum = [0]
sum = 0

for i in range(n):
    sum += array[i]
    prefix_sum.append(sum)


for i in range(m):
    x, y = map(int, input().split())
    print(prefix_sum[y] - prefix_sum[x-1])