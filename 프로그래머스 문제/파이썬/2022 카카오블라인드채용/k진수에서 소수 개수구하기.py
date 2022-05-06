import sys
import math

def is_prime_num(n : int) -> bool:
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n,k):
    num = ''
    stack = []
    cnt = 0
    while n:
        q,r = divmod(n,k) # 몫과 나머지
        n = q
        stack.append(str(r))
    
    while stack:
        num += stack.pop()
    
    stack = list(num.split('0'))
    print(stack)
    for i in stack:
        if i and is_prime_num(int(i)):
            cnt += 1

    return cnt
if __name__ == '__main__':
    a = [[437674,3],[110011,10]]
    for i in a:
        n,k = i
        print(solution(n,k))