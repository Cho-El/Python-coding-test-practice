#
# 1번 풀이 시간초과
# from math import gcd
# import sys

# t = int(input())
# for _ in range(t):
#     m,n,x,y = map(int, sys.stdin.readline().split())

#     sx = 0
#     sy = 0
#     year = 0
#     check = 0
#     while sx <= m and sy <= n:
#         year += 1
#         sx += 1
#         sy += 1
#         if sx == m and sy == n:
#             break
#         if x == sx and y == sy: # 해를 찾는다
#             check = 1
#             break
#         if sx > m:
#             sx %= m
#         if sy > n:
#             sy %= n
    
#     if check == 1:
#         print(year)
#     else:
#         print(-1)

# 2번 풀이 50퍼 시간초과
'''
문제 힌트
m,n의 마지막 해는 최소공배수
Year를 m으로 나누었을 때 나머지가 x
Year를 n으로 나누었을 때 나머지가 y
'''
# import sys
# from math import gcd

# t = int(input())
# for _ in range(t):
#     m,n,x,y = map(int, sys.stdin.readline().split())
#     last_year = m * n // gcd(m,n)
#     year = 0
#     a, b = 0, 0
#     while year <= last_year:
#         year = a * m + x
#         year2 = b * n + y

#         if year == year2:
#             break
#         while year < year2:
#             a += 1
#             year = a * m + x
#             if year == year2:
#                 break
#         else:
#             b += 1
#             continue
#         break
#     else:
#         year = -1
#     print(year)

# 3번 풀이
import sys
from math import gcd

t = int(input())
for _ in range(t):
    m,n,x,y = map(int, sys.stdin.readline().split())
    last_year = m * n // gcd(m,n)
    year = 0
    a, b = 0, 0
    while year <= last_year:
        year = a * m + x
        if (year - y) % n == 0:
            break
        a += 1
    else:
        year = -1
    print(year)