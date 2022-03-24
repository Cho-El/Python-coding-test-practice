import sys
from itertools import combinations as com
n = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))
dice_sum = []
dice_idx = [0,1,2,3,4,5]

min1 = min(dice[0],dice[5])
min2 = min(dice[1],dice[4])
min3 = min(dice[2],dice[3])

temp = [min1,min2,min3]
temp.sort()
total = 0
for i in range(3):
    total += temp[i]
    dice_sum.append(total)

if n == 1:
    dice.sort()
    result = sum(dice[:-1])

else:
    r1 = (n-2) * (n-1) * 4 + (n-2) * (n-2)
    r2 = (n-1) * 4 + (n-2) * 4
    r3 = 4

    result = r1 * dice_sum[0] + r2 * dice_sum[1] + r3 * dice_sum[2]

print(result)
# remove 이슈 기억
'''
리스트에서 값을 비교하다 중간에 삭제하는 경우,
index를 하나 건너뛰어서 검사하는 경우가 생길 수 있다. 주의하기 바란다.

'''