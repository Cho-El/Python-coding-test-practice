'''
에라토스테네스의 체 알고리즘
다수의 자연수에 대하여 소수 여부를 판별할 때 사용하는 대표적인 알고리즘입니다.
동작 과정
1. 2부터 N가지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다.
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.
'''

import math
def is_prime_nmber(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False # 소수 아님
    return True # 소수

def eratoss(n):
    array = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1) :
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    
    for i in range(2, n + 1): #모든 소수 출력
        if array[i]:
            print(i)