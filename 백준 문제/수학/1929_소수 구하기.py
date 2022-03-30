import math
# 소수 판정 수학 에라토스테네스의 체
# 1번 풀이 ---------------------------
m,n = map(int, input().split())
def prime_number(n):
    check = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            check = False
            break
    
    if check:
        print(n)

for i in range(m, n+1):
    if i == 1:
        continue
    prime_number(i)

# 2번 풀이
# m,n = map(int, input().split())

# def eratoss(m,n):
#     array = [True for i in range(n + 1)]

#     for i in range(2, int(math.sqrt(n)) + 1) :
#         if array[i] == True:
#             j = 2
#             while i * j <= n:
#                 array[i * j] = False
#                 j += 1
    
#     for i in range(m, n + 1): #모든 소수 출력
#         if array[i]:
#             print(i)

# eratoss(m,n)