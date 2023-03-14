# 분할정복
import sys
n = int(input())

def add_star(n):
    if n == 3:
        return ['***','* *','***']
    
    Star = add_star(n//3)
    temp_star = []
    # 상단
    for top in Star:
        temp_star.append(top * 3)
    # 중단
    for middle in Star:
        temp_star.append(middle + ' ' * (n//3) + middle)
    # 하단
    for bottom in Star:
        temp_star.append(bottom * 3)
    
    return temp_star

for i in add_star(n):
    print(i)