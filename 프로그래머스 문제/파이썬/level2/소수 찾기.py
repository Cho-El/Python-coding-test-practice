from itertools import permutations as per
import math

def is_prime_number(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수 아님
    return True # 소수

def solution(numbers):
    n_list = []
    results = []
    cnt = 0
    for i in range(1, len(numbers)+1):
        n_list = list(per(numbers,i))
        for n in n_list:
            temp = ''.join(n)
            results.append(int(temp))
    set_result = set(results)

    for result in set_result:
        if is_prime_number(result):
            print(result)
            cnt += 1
    return cnt

numbers = '011'
print(solution(numbers))