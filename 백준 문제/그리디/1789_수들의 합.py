# 그리디
import sys
input = sys.stdin.readline
S = int(input())
temp = 1
result = 0
while S >= temp:
    S -= temp
    temp += 1
    result += 1

print(result)