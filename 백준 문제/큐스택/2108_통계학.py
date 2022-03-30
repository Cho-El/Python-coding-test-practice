import sys
# 수학 구현 정렬
from bisect import bisect_left
from bisect import bisect_right

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

print(num)
num2 = set(num)
num.sort()
print(round(sum(num)/n))
print(num[n//2])
temp = []
for n2 in num2:
    l = bisect_left(num,n2)
    r = bisect_right(num,n2)
    temp.append((r-l,n2))
temp.sort(key = lambda x : x[1])
temp.sort(reverse = True, key = lambda x : x[0])
if len(temp) != 1 and temp[0][0] == temp[1][0]:
    print(temp[1][1])
else:
    print(temp[0][1])
print(max(num)-min(num))