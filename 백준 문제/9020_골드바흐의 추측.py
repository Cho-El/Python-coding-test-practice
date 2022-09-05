#
import math
import sys
input = sys.stdin.readline

n = int(input())
# 에라토스테네스의 체
array = [True for _ in range(10001)]
for i in range(2, int(math.sqrt(10000)) + 1):
    j = 2
    while i * j <= 10000:
        array[i * j] = False
        j += 1
        
for _ in range(n):
    target = int(input())
    partition = []
    for i in range(2, target + 1):
        if array[i] and array[target-i]:
            temp = sorted([target - i, i])
            if partition:
                if partition[1] - partition[0] > temp[1] - temp[0]:
                    partition = temp
            else:
                partition = temp
                
    print(*partition)