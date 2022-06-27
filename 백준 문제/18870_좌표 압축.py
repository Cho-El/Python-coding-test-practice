# 리스트 내 정수에서 그 정수보다 큰거나 작은 것의 개수를 구하는 경우 set로 중복을 빼주는 게 좋다.
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().rstrip().split()))
array2 = list(set(array))
array2.sort()

array_cnt = {}
temp = 0
for a in array2:
    array_cnt[a] = temp
    temp += 1
    
for a in array:
    print(array_cnt[a], end = ' ')