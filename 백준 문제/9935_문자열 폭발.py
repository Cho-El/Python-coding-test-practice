#
import sys

input = sys.stdin.readline
target = input().rstrip()
explosion = input().rstrip()

# 문자열 안에 폭발 문자가 있는지 체크
temp = []
for i in range(len(target)):
    temp.append(target[i])
    if ''.join(temp[-len(explosion):]) == explosion:
        for i in range(len(explosion)):
            temp.pop()

if temp:
    print(''.join(temp))
else:
    print('FRULA')