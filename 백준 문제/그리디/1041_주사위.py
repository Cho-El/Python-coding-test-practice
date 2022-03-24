import sys
from itertools import combinations as com
n = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))
dice_sum = []
dice_index = [0,1,2,3,4,5]
ex = [(0,5),(1,4),(2,3)] # 마주보는 두 면의 인덱스
# 한 면만 보일 때
dice_sum.append(min(dice))

# 두 면만 보일 때
temp = []
for i in range(len(dice)-1):
    for j in range(i+1, len(dice)):
        if (i,j) in ex:
            continue
        temp.append(dice[i] + dice[j])
dice_sum.append(min(temp))

# 세 면만 보일 때
temp = []
for i in range(len(dice)-2):
    for j in range(i+1, len(dice)-1):
        if (i,j) in ex:
            continue
        for l in range(j+1, len(dice)):
            if (j,l) in ex or (i,l) in ex:
                continue
            temp.append(dice[i] + dice[j] +dice[l])

dice_sum.append(min(temp))


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