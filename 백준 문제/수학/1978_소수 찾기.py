import math
# 소수 판정 수학 에라토스테네스의 체

n = int(input())
l = list(map(int, input().split()))

result = 0

def prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    
    return True
for i in l:
    if prime_num(i):
        result += 1

print(result)